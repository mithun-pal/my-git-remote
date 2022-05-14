import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from util.getconf import read_conf


if __name__ == "__main__": 
    cnfg = read_conf()
    print("value of key1: ", cnfg["feature1"]["key1"])
