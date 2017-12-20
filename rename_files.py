
import os
def renamefiles():
    file_list=os.listdir(r"E:\work\DEMO VIDEOS\MEDICENTRE VIDEO GUIDE FILES")
    saved_path=os.getcwd()
    print("current directory"+ saved_path)
    os.chdir(r"E:\work\DEMO VIDEOS\MEDICENTRE VIDEO GUIDE FILES")
 
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))

renamefiles()
         
