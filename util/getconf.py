import os
import configparser


def read_conf():
    script_path = os.path.abspath(__file__)
    script_root_dir = "\\".join(script_path.split("\\")[0:-2])
    config = configparser.ConfigParser()
    config.read(f"{script_root_dir}/conf/myapp.cnf")
    return config
    
    
if __name__ == "__main__":
    read_conf()
    
