import os
import pdb

def language_pkm(file_list):
    language = ""
    PKM = "" 
    # language , package manager
    print(file_list)
    suffix = []
    # pdb.set_trace()
    for file in file_list:
        if "." in file:
            suffix += file.split(".")[1]
    
    if "pom.xml" in file_list:
        language = "Java"
        PKM = "Maven"
    elif "build.gradle" in file_list:
        language = "Java"
        PKM = "Gradle"
    elif "build.xml" in file_list:
        language = "Java"
        PKM = "Ant"
    elif "shrinkwrap.json" or "package-lock.json" or "package.json" in file_list:
        language = "JS"
        PKM = "NPM"
    elif "yarn.lock" or "package.json" in file_list:
        language = "JS"
        PKM = "Yarn"
    elif "podfile.lock" in file_list:
        language = "OC"
        PKM = "CocoaPods"
    elif "composer.lock" or "composer.json" in file_list:
        language = "PHP"
        PKM = "Composer"
    elif "setup.py" or "requirements.txt" in file_list:
        language = "Python"
        PKM = "pip"
    elif "Pipfile" or "Pippfile.lock" in file_list:
        language = "Python"
        PKM = "Pipenv"
    elif "gemfile.lock" in file_list:
        language = "Ruby"
        PKM = "Rubygems"
    elif "build.sbt" in file_list:
        language = "Scala"
        PKM = "SBT"
    elif "environment.yml" in file_list:
        language = "R or Python"
        PKM = "Conda"
    elif "go.mod" or "go.sum" in file_list:
        language = "go"
        PKM = "Moudles"
    elif "sln" in suffix:
        language = "C#"
        PKM = "NuGet_*"

    return language,PKM

if __name__ == "__main__":
    repo_path = "C:\\Users\\syt\\Desktop\\repo\\java-goof-master"
    list = os.listdir(repo_path)
    print(language_pkm(list)) 
