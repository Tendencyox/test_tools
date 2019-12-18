from __future__ import print_function
import ctypes, sys
import os
import subprocess
import time
path = "C:/Users/syt/Desktop/repo/pip-master"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
def detect(path):
    # os.system("java -jar C:/Users/syt/Desktop/scantist-bom-detect.jar -airgap")
    subprocess.Popen(
        "java -jar C:/Users/syt/Desktop/scantist-bom-detect.jar -airgap",
        shell = True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    files = os.listdir(path)
    # print(files)
    flag = 0
    for file in files:
        if file == "dependency-tree.json":
            flag = 1
    if flag == 0:
        return -1
    f = open(path + r"/" + file)
    iter_f = iter(f)
    str = ""
    for line in iter_f:
        str += line
    if str:
        return 1
    else:
        return -2


if is_admin():
    res = detect(path)
    print(res)
    time.sleep(2000)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)