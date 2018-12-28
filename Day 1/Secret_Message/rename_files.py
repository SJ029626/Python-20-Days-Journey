import os

def rename_files():
    #get filenames
    #os.chdir(r"C:\Users\MercurySky\Desktop\Python Projects\Secret_Message\prank")
    file_list = os.listdir(r"C:\Users\MasterMind\Desktop\Python Projects\Secret_Message\prank")
    for file_name in file_list:
        #rename each file, removing numbers
        #print file_name
        os.rename(file_name, file_name.translate(None, '0123456789'))
        #print file_name
rename_files()
