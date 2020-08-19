# !/usr/bin/env python
import yaml,os

class readconfig:

    def read_config(self):
        # 获取当前文件路径
        root_path = os.path.dirname(os.path.dirname(__file__))
        # 获取项目根目录
        # filepath = os.path.abspath('..')
        configpath=os.path.join(root_path,'application.yml')
        # print(configpath)
        #从根目录开始找配置文件并打开
        with open(configpath, 'r', encoding="utf-8") as f:
            # load方法转出为字典类型
            x = yaml.load(f.read(),Loader=yaml.FullLoader)
            return x

if __name__ == '__main__':
    r1=readconfig()
    r1.read_config()