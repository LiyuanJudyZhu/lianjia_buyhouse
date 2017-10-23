#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import xlwt
import sys,time, re
import csv

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

'''
# 获取代理ip在爬取链家信息时暂未使用
def getListProxies():
    session = requests.session()
    page = session.get("http://www.xicidaili.com/nn/1", headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'lxml')

    proxyList = []
    taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    for trtag in taglist:
        tdlist = trtag.find_all('td')
        proxy = {'http': 'http://'+tdlist[1].string + ':' + tdlist[2].string,
                 'https': 'http://'+tdlist[1].string + ':' + tdlist[2].string}

        print(proxy)
        url = "http://ip.chinaz.com/getip.aspx"  #用来测试IP是否可用的url
        #response = session.get(url, proxies=proxy, timeout=5)
        #print(response.status_code) 
        try:
            response = session.get(url, proxies=proxy, timeout=1)
            print(response.status_code) 
            print(proxy)
            proxyList.append(proxy)
            if(len(proxyList) == 10):
                break
        except Exception as e:
            print('failed')
            continue
        else:
            print('sucess!!!')
            # web_url = requests.get('http://cd.fang.lianjia.com/loupan/pg',proxies=proxy, headers = headers)
            # print(web_url.status_code) #HTTP状态码有5种，
            # # 所有状态码的第一个数字代表了响应的5种状态之一：
            # # (1)消息：1XX；(2)成功：2XX;(3)重定向：3XX;(4)请求错误：4XX;(5)服务器错误：5XX.
            # print(web_url.url)
    return proxyList
'''
#获取每页的url链接#
def get_page_url(url):
    global headers
    web_url = requests.get(url,headers = headers)
    print(web_url.status_code) #HTTP状态码有5种，所有状态码的第一个数字代表了响应的5种状态之一：(1)消息：1XX；(2)成功：2XX;(3)重定向：3XX;(4)请求错误：4XX;(5)服务器错误：5XX.
    web_url_soup = BeautifulSoup(web_url.text,'lxml')
    page_urls = web_url_soup.select('#house-lst > li > div > div.col-1 > h2 > a')
    for page_url in page_urls:
        each_url = "http://cd.fang.lianjia.com" + page_url.get('href')
        get_detail_info(each_url)

# 获取房源详细信息
def get_detail_info(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    titles = soup.select('title')
    addresses = soup.select('p.where > span')
    prices = soup.select('p.jiage')
    open_time = soup.select('p.when')
    global count
    global count2
    count +=1
    # print(url)
    # print(titles)
    # print(addresses)
    # print(prices)
    # print(open_time)
    
    for title, address, price,open_time in zip(titles, addresses, prices, open_time):
        address = address.attrs
        price = price.get_text().strip().split()[1]
        data = {
            'url':url,
            'title': title.get_text(),
            'address': address["title"],
            'price': price,
            'open_time': open_time.get_text().strip()
        }
        for key in data:
            print (key, ":",data[key])
        count2 +=1
        list_data = [data["address"], data["title"],data["url"], data["price"]]
        writer.writerow(list_data)

count = 0
count2 = 0
if __name__ =="__main__":
    fileobj=open('lianjia.csv','a')#注意是a
    #可以理解为初始化
    writer = csv.writer(fileobj)#csv.writer(fileobj)返回writer对象writer
    lsit = ['address', 'title', 'url', 'price']
    writer.writerow(lsit)

    urls = ["http://cd.fang.lianjia.com/loupan/pg{}/".format(number) for number in range(1, 92)]
    import gevent
    from gevent import monkey
    monkey.patch_all()
    proxies={'http':'http://127.0.0.1:6666', 'https':'https://127.0.0.1:6666'}
    def list_gevent(n):
        list_g = []
        for index in range(n):
            list_g.append(gevent.spawn(get_page_url, urls[index]))
        return list_g

    start_time = time.time()
    gevent.joinall(list_gevent(91))
    end_time = time.time()
    print("time cost:",end_time - start_time)
    fileobj.close()
    print("count:",count)
    print("count2:",count2)