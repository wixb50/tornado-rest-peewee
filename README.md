# Tornado Rest Peewee使用范例

## 部署步骤

1.安装运行
```
pip install -r requirements.txt
python setup.py install
```

2.初始化数据库(先手动创建db)
```
python tornado_rest_peewee/models/migrate.py
```

3.启动进行运行
```
python -m tornado_rest_peewee runserver -p 8050 # 不传默认为8050
```

## 部署规范建议(供参考)

1.镜像范例

代码示例中`Dockerfile-base`为基础镜像，用于安装系统的依赖包；

代码示例中`Dockerfile`为业务镜像，用于部署代码运行；

2.部署范例

代码示例中`supervisor.conf`在容器中建议采用supervisor作为进程管理工具；

并且支持一个容器中运行多个进程；

需在上层增加nginx反向代理作为负载均衡入口。
