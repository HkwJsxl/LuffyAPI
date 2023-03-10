# 路飞项目

vue前端：https://github.com/HkwJsxl/luffycity

## 项目目录

> ├── LuffyAPI
> 
> 	├── resources/		外部资源文件夹
> 
> 	├── celery_task/		celery - 包
>	
> 	├── logs/		项目开发日志目录 - 包
>	
> 	├── manage.py		 测试运行脚本
> 
> 	├── manage_pro.py		 上线运行脚本
>	
> 	├── LuffyAPI/		项目主应用，开发时的代码保存 - 包
>	
> 	├── apps/ 		开发者的代码保存目录，以模块[子应用]为目录保存 - 包
>	
> 		├── views/		所有应用的视图文件 - 包
> 			
> 		└── serializers/		所有应用的序列化文件 - 包
>	
> 	├── libs/		第三方类库的保存目录[第三方组件、模块] - 包
>	
> 	├── settings/		配置目录 - 包
>	
> 		├── const.py		配置文件常量
> 
> 		├── dev.py		项目开发时的本地配置
> 			
> 		└── pro.py		项目上线时的运行配置
>	
> 	├── urls.py		总路由
>	
> 	└── utils/		多个模块[子应用]的公共函数类库[自己开发的组件]
>	
> 	└── scripts/		保存项目运营时的脚本文件或自测脚本 - 文件夹 (不上传)
> 
> 	├── Dockerfile		 dockerfile部署文件
> 
> 	├── docker-compose.yml		 docker-compose部署文件

## 功能

~~~
0.自定义验证，异常处理，分页，mixins，响应对象，返回值，短信发送频率限制
1.解决跨域，记录日志
2.首页轮播图
3.注册，登录多方式，JWT认证
4.redis，celery缓存，更新轮播图缓存
5.课程分类，课程章节
6.搜索课程
7.支付宝支付，订单详情
8.docker部署，dockerfile部署，docker-compose部署(https://www.cnblogs.com/hkwJsxl/p/17164139.html)
~~~
