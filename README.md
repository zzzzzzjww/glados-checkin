# 怎么说 看运气签到








# glados-checkin
  每天自动签到（天数+1），自动推送结果  


# Github Actions说明
## 一、Fork此仓库
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置账号密码

添加名为——值分别为：  
**SERVE**  ——**on/off** 你想你的serve酱开不开启通知  
**SCKEY**  ——**sckey**  开的话填你的serve酱的sckey，不开就不填   
**COOKIE** —— **cookie** 弄上你账号的cookie  
暂不支持多账号，懒得弄
![](http://tu.yaohuo.me/imgs/2020/06/748bf9c0ca6143cd.png)

## 三、启用Action
1 点击**Action**，再点击**I understand my workflows, go ahead and enable them**  
2 修改任意文件后提交一次  
![](http://tu.yaohuo.me/imgs/2020/06/34ca160c972b9927.png)

## 四、查看运行结果
Actions > Cloud189Checkin > build  
能看到如下图所示，表示成功，或者看你微信通知  
![](http://tu.yaohuo.me/imgs/2020/06/289432b53bded61c.png)  
  
# 腾讯云函数
复制py代码，将三个参数自行修改  



此后，将会在每天半夜12点多会自动签到一次  
若有需求，可以在[.github/workflows/python-publish.yml]中自行修改  
