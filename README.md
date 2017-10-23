## 基于python beautifulsoup爬取链家网成都地区新房源，并用高德api在地图上可视化显示

一.使用方法
- 1.工程里面已经有爬取后的lianjia.csv文件，可以删除，然后执行buy_house.py即可生成csv文件

- 2.爬取完成后，在工程目录下执行命令`python -m http.server 3000`,然后打开`http://localhost:3000/`,点击打开map.html，导入上面生成的lianjia.csv文件即可。(Python内置了一个简单的HTTP服务器,只需要在命令行下面敲一行命令,一个HTTP服务器就起来了: python -m SimpleHTTPServer,我用python3.5 改为python -m http.server即可),导入后鼠标放在蓝色表示的房源位置上会自动显示出地址和房价信息。

- 3.效果图如下

![Image text](https://github.com/codingMrHu/lianjia_buyhouse/blob/master/img/home.png)
![Image text](https://github.com/codingMrHu/lianjia_buyhouse/blob/master/img/%E6%95%B4%E4%BD%93.png)


二.实现思路

1.beautifulsoup及协程爬取房源信息
爬取的是链家网的成都地区的新房源，爬出房源的地址、名字、url，价格这四个。我是基于python的beautifulsoup实现爬虫的，爬取数据的时候没有遇到ip限制的问题，所以并未使用ip代理，为了提高爬取速率采用“协程”进行处理。

2.高德地图API调用
采用高德地图对房源进行可视化操作，在工程根目录下创建map.html文件，页面大框架可直接从示例中心复制：高德 JavaScript API 示例中心http://lbs.amap.com/api/javascript-api/example/map/map-show/。
高德可视化的实现参考：http://www.jianshu.com/p/4ce0b0588fa3
