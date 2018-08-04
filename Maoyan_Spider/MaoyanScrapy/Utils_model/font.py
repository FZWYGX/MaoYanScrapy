import requests
import re
import os
from fontTools.ttLib import TTFont


def font_creator(html):
    """
    这个函数是用来处理动态数字加载问题
    :param html:
    :return:饭后的是处理之后，带有正确数字的html代码
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    # 用正在表达式匹配后缀为woff的url
    woff_name = re.search(r"url\('//vfile.meituan.net/colorstone/(.*\.woff)'\)", html).group(1)

    # 判断文件是否存在，不存在再下载
    file_list = os.listdir('./fonts')
    if woff_name not in file_list:
        woff_url = 'http://vfile.meituan.net/colorstone/' + woff_name
        response_woff = requests.get(woff_url, headers=headers).content
        with open('./fonts/' + woff_name, 'wb') as f:
            f.write(response_woff)

    # 手动解析一组basefonts.woff的映射
    baseFonts = TTFont('./fonts/basefonts.woff')
    base_nums = ['9', '4', '2', '1', '3', '7', '8', '0', '6', '5']
    base_fonts = ['uniECE2', 'uniF284', 'uniF5F6', 'uniE3CA', 'uniF798', 'uniF7E7', 'uniF020', 'uniE4A7', 'uniF4B5',
                  'uniE0FC']

    # 调用在线下载的
    onlineFonts = TTFont('./fonts/' + woff_name)
    uni_list = onlineFonts.getGlyphNames()[1:-1]
    temp = {}
    # 解析字体库，通过我们给出的，和新下载的做比对
    for i in range(10):
        onlineGlyph = onlineFonts['glyf'][uni_list[i]]
        for j in range(10):
            baseGlyph = baseFonts['glyf'][base_fonts[j]]
            if onlineGlyph == baseGlyph:
                temp["&#x" + uni_list[i][3:].lower() + ';'] = base_nums[j]

    # 字符替换
    pat = '(' + '|'.join(temp.keys()) + ')'
    html = re.sub(pat, lambda x: temp[x.group()], html)
    # 返回是正确数字的html源码
    return html
