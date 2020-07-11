import yaml,os

def red_data(feil_name):
    file_path = os.getcwd() + os.sep + 'data' + os.sep + feil_name
    with open(file_path,'r',encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data

def read_yaml(file_name):
    file_path = os.getcwd() +os.sep + 'data' + os.sep + file_name + '.yaml'
    with open(file_path,'r' ,encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data
