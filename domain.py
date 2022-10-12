# encoding=utf8

from itertools import combinations_with_replacement
import whois
import logging
import requests


def logger_config(log_path,logging_name):
    '''
    配置log
    :param log_path: 输出log路径
    :param logging_name: 记录中name，可随意
    :return:
    '''
    '''
    logger是日志对象，handler是流处理器，console是控制台输出（没有console也可以，将不会在控制台输出，会在日志文件中输出）
    '''
    # 获取logger对象,取名
    logger = logging.getLogger(logging_name)
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    logger.setLevel(level=logging.DEBUG)
    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    # 生成并设置文件日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # console相当于控制台输出，handler文件输出。获取流句柄并设置日志级别，第二层过滤
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # 为logger对象添加句柄
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger
 

def domain(count):
    # suffix = ['.com', '.cn', '.top', '.xyz', '.net', '.ltd', '.vip', '.shop', '.cc', '.store', '.online', '.fun', '.tech', '.art', '.site', '.co', '.icu', '.club', '.work', '.xin', '.wang', '.space', '.group', '.ink', '.pub', '.info', '.ren', '.live', '.link', '.cloud', '.com.cn', '.我爱你', '.中国', '.网址', '.website', '.pro', '.life', '.tv', '.asia', '.biz', '.cool', '.mobi', '.fit', '.公司', '.网络', '.plus', '.press', '.wiki', '.love', '.red', '.design', '.video', '.run', '.show', '.zone', '.kim', '.city', '.gold', '.today', '.host', '.team', '.chat', '.fund', '.beer', '.center', '.company', '.email', '.yoga', '.luxe', '.net.cn', '.org.cn', '.world', '.fans', '.guru', '.在线', '.商店', '.企业', '.集团', '.招聘', '.网店', '.商城', '.中文网', '.佛山', '.广东', '.商标', '.游戏', '.娱乐', '.餐厅', '.law', '.social', '.gov.cn']
    suffix = ['.com', '.cn', '.top', '.xyz', '.net', '.ltd', '.vip', '.shop', '.cc', '.store', '.online', '.fun', '.tech', '.art', '.site', '.co', '.icu', '.club', '.work', '.xin', '.wang', '.space', '.group', '.ink', '.pub', '.info', '.ren', '.live', '.link', '.cloud', '.我爱你', '.中国', '.网址', '.website', '.pro', '.life', '.tv', '.asia', '.biz', '.cool', '.mobi', '.fit', '.公司', '.网络', '.plus', '.press', '.wiki', '.love', '.red', '.design', '.video', '.run', '.show', '.zone', '.kim', '.city', '.gold', '.today', '.host', '.team', '.chat', '.fund', '.beer', '.center', '.company', '.email', '.yoga', '.luxe', '.world', '.fans', '.guru', '.在线', '.商店', '.企业', '.集团', '.招聘', '.网店', '.商城', '.中文网', '.佛山', '.广东', '.商标', '.游戏', '.娱乐', '.餐厅', '.law', '.social']
    items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for index in range(count):
        logger.info("获取"+str(index + 1)+"位域名")
        for c in combinations_with_replacement(items,index + 1):
            arr = list(c)
            domain = ''.join(arr)
            for i in range(len(suffix)):
                h = domain + suffix[i]
                try:
                    whois.whois(h)
                except whois.parser.PywhoisError:
                    logger.info(h)
                    sendWX(h)
def sendWX(content):
    url = 'http://www.pushplus.plus/send?token=da5fa19b1f804d41bcd64080be38fcff&title='+content+'&content='+content
    requests.get(url)                    

if __name__ == "__main__":
    logger = logger_config(log_path='log.txt', logging_name='就靠你了')
    for index in range(1000):
        domain(2)
