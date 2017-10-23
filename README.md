## 基于python beautifulsoup爬取链家网成都地区新房源，并用高德api在地图上可视化显示

- 1.效果图如下
![Image text](https://github.com/codingMrHu/lianjia_buyhouse/blob/master/img/home.png)
![Image text](https://github.com/codingMrHu/lianjia_buyhouse/blob/master/img/%E6%95%B4%E4%BD%93.png)

- 2.工程里面已经有爬取后的rent.csv文件，可以删除，然后执行buy_house.py即可生成csv文件

- 3.爬取完成后，执行命令`python -m http.server 3000`,然后打开`http://localhost:3000/`,点击打开map.html，导入上面生成的rent.csv文件即可。