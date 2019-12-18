import os
from find_language import language_pkm
from build import build_proj
from bom import airgap

repo_path = "C:/Users/syt/Desktop/repo"

            
    
def main(floder_path):
    # list of filename in floder
    file_list = os.listdir(floder_path)
    #  first step: find out language
    res_lang,res_pkm = language_pkm(file_list)
    #  second step: whether can be build
    res = build_proj(floder_path, res_lang, res_pkm)
    if res == 0:
        res = airgap(floder_path)
    else :
        #  some operations
        return

  
if __name__ == "__main__":
    floders = os.listdir(repo_path)
    os.chdir(repo_path)
    for floder in floders:
        main(repo_path + "/" + floder)
    