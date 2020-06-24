import yaml

def get_yaml_data(yaml_file):
    # 打开yaml文件
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()


    data = yaml.load(file_data)
    return data