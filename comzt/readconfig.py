# !/usr/bin/env python
import os,yaml

class readconfig:

    def conf(self):
        # 获取当前文件路径
        root_path = os.path.dirname(__file__)
        # 获取项目根目录
        filepath = os.path.abspath('..')
        # 获取yaml配置文件路径
        yamlPath = os.path.join(filepath, 'application.yaml')
        # 打开配置文件
        f = open(yamlPath, 'r', encoding='utf-8')
        # 创建读取对象
        cont = f.read()
        x = yaml.load(cont)
        return x;