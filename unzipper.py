import zipfile
import os
import pandas as pd 

def unzipper():
    extension = ".zip"
    name_list = pd.read_csv("filename.csv")
    newname = "%s.csv"
    name_list_for_zipping = pd.read_csv("filename_zipper.csv")
    for indx in name_list_for_zipping.index: # for item in os.lisdir():
        # if item.endswith(extension):
            # file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(name_list_for_zipping['0'][indx])
            zip_ref.extractall('C:/Users/pillai_amal/bhavcopy')
            zip_ref.close()

    os.chdir('C:/Users/pillai_amal/bhavcopy')

    list_of_files = os.listdir()
    len_of_files = len(list_of_files)

    if not os.listdir():
        for indx in name_list.index:
            os.rename(name_list['0'][indx], newname % (indx))
    else:
        for indx in name_list.index:
            os.rename(name_list['0'][indx], newname % (len_of_files - 1))