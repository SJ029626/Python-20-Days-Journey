import os

def rename_files():
    #(1) get file names from a folder
    os.chdir(r"C:\Users\MercurySky\Desktop\35 Days of code\Day 1\Secret_Message\alphabet")
    file_list = os.listdir(r"C:\Users\MercurySky\Desktop\35 Days of code\Day 1\Secret_Message\alphabet")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
