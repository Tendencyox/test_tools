import os
import subprocess

def airgap(path):
    #  res = -1 stand for cannnot use airgap
    #  res = 1 stand for run successfully
    #  res = -2 stand for run successfully but dependency_tree is empty
    os.chdir(path)
    subprocess.run("java -jar C:/Users/syt/Desktop/scantist-bom-detect.jar -airgap")
    files = os.listdir(path)
    # print(files)
    flag = 0
    for file in files:
        if file == "dependency-tree.json":
            f = open(path + r"/" + file)
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str += line
            if str:
                return 1
            else:
                return -2
            flag = 1
    if flag == 0:
        return -1

if __name__ == "__main__":
    floder_path = "C:/Users/syt/Desktop/repo/example-maven-travis-master"
    res = airgap(floder_path)
    print(res)