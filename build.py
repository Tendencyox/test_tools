import os
import pdb
import subprocess
# this function is to build the project
# floder_path is the project root path
def build_Csharp():
    return 

def build_java(path, pkm):
    # package manager: Maven, Gradle, Ant
    # successful singal: build successful in log doc
    os.chdir(path)
    if pkm == "Maven":
        os.system("mvn package > log.txt")
    elif pkm == "Gradle":
        os.system("gradle build > log.txt")
    else :
        os.system("ant > log.txt")
    
    line = ""
    flag = 0

    # pdb.set_trace()

    fp = open(path + "/" + "log.txt")
    lines = fp.readlines()
    for line in lines:
        if "build success" in line.lower():
            flag = 1
    fp.close()

    # pdb.set_trace()

    return flag

def build_js(path, pkm):
    # package manager: npm, yarn
    # successful signal: dependency.json exist
    os.chdir(path)
    if pkm == "npm":
        os.system("npm insatll")
    elif pkm == "yarn":
        os.system("yarn install")
    files = os.listdir(path)
    flag = 0
    if "package_lock.json" in files:
        flag = 1
    return flag

def build_oc(path, pkm):
    # package manager: CocoaPods
    # successful signal: no data
    # no data 
    return 0


def build_php(path, pkm):
    # package manager:composer 
    os.chdir(path)
    if pkm == "composer":
        cmd = "composer install"
    try:
        subprocess.run(cmd)
    except OSError:
        return 0
    return 1 

def build_py(path, pkm):
    # package manager: pip, pipenv
    # only can use python exception to verify success or not
    os.chdir(path)
    cmd = ""
    if pkm == "pip":
        cmd = "pip install -r requirements.txt --log log.txt"
    else:
        cmd = "pipenv install"
    # pdb.set_trace()
    try:
        subprocess.run(cmd)
    except OSError:
        return 0
    return 1

def build_rb(path, pkm):
    # package manager: RubyGems
    # same as former one
    os.chdir(path)
    cmd = "ruby -c "
    files = os.listdir(path)
    for file in files:
        if ".rb" in file:
            tmp = cmd + file
            try:
                subprocess.run(tmp)
            except OSError:
                return 0
    return 1

def build_go(path, pkm):
    # package manager: Modules
    # same as former one
    os.chdir(path)
    cmd = "go build"
    try:
        subprocess.run(cmd)
    except OSError:
        return 0
    return 1

def build_conda(path, pkm):
    # package manager: conda
    # language: R or Python
    # same as former one 
    os.chdir(path)
    cmd = "conda build"
    try:
        subprocess.run(cmd)
    except OSError:
        return 0
    return 1 
    


def build_proj(path, lang, pkm):
    # language : C#,Java,Python,Js,OC,PHP,Ruby,Scala,Go ,etc.
    os.chdir(path)
    res = -3
    if lang == "C#":
        res = build_Csharp(path)
    elif lang == "Java":
        res = build_java(path, pkm)
    elif lang == "JS":
        res = build_js(path, pkm)
    elif lang == "OC":
        res = build_oc(path, pkm)
    elif lang == "PHP":
        res = build_php(path, pkm)
    elif lang == "Python":
        res = build_py(path, pkm)
    elif lang == "Ruby":
        res = build_rb(path, pkm)
    elif lang == "go":
        res = build_go(path, pkm)
    elif lang == "R or Python":
        res = build_conda(path, pkm)
    return res

if __name__ == "__main__":
    # floder_path = "C:/Users/syt/Desktop/repo/example-maven-travis-master"
    # language = "Java"
    # package_manager = "Maven"
    floder_path = "C:/Users/syt/Desktop/repo/pip-update-requirements"
    language = "Python"
    package_manager = "pip"
    res = build_proj(floder_path, language, package_manager)
    print(res)