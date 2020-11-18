#
#requirement: pip install mega.py
#dev: imshawan
#
import os
import sys
import creds
from mega import Mega
from time import sleep
print("        Please wait while I load your account...")
mega = Mega()
m = mega.login(creds.username, creds.paswd)
print("        Logged in successfully")
sleep(0.5)

def get_details():
    details = m.get_user()
    print("        Email: " + details.get('email'))
    print("        Name: " + details.get('name'))

def bal():
    bal = m.get_balance()
    print("        Your Balance is: %s" %bal)
    
def quota():
    quota = m.get_quota()
    print("        Your Storage Quota is: %s Megabytes" %quota)

def get_storageInfo(): #get account Storage details
    # Use output kilo, mega, giga, or else bytes will be default output
    space = m.get_storage_space(mega=True)
    total = space.get('total')
    print("        Total Space Avaliable: %s Megabytes" %total)
    used = space.get('used')
    print("                   Used Space: %s Megabytes" %used)
    

def get_filenames():
    print("        NOTE: Filenames Without any Extensions(.pdf,.txt,.mp3 etc.) are folders")
    i = 0
    j = 1
    files = m.get_files()
    for f in files:
        filename = files[f]['a']['n']
        filenm = str(filename)
        i +=1
        if i>3:
            print("           ",j,"|" + " %s " %filenm)
            j+=1

def create_fol():
    name = input("        Enter Folder name to be created: ")
    m.create_folder(name)
    print("        Folder Created!")

def upload_file():
    file_name = input("        Enter Filename/Folder If stored in current Folder): ")
    ans = input("        TYPE 'ROOT' to upload the file/folder in ROOT Directory \nOR to upload the file/folder in a Folder, Enter Foldar name:")
    if ans == 'ROOT' or ans == 'root':
        files = m.upload('new.txt')
        print("        File Uploaded!")
        linkurl = m.get_upload_link(files)
        print("        File URL: \n%s" %linkurl)
    else:
        try:
            folder = m.find(ans, exclude_deleted=True)
            files = m.upload(file_name, folder[0])
            print("        File Uploaded!")
            linkurl = m.get_upload_link(files)
            print("        File URL: \n%s" %linkurl)
        except TypeError:
            print("        No Such folder found!")

def find_file_folder():
    fname = input("        Enter File/Folder Name to Find: ")
    fr = m.find(fname, exclude_deleted=True)
    if fr == None:
        print("        NO such folder exists")

def download():
    ans = input("        1. By File/FolderName \n2. BY URL \nEnter Selection: ")
    if ans == '1':
        ffname = input("        Enter File/FolderName: ")
        file = m.find(ffname)
        try:
            m.download(file)
            loc = os.getcwd()
            print("        File downloaded to: %s" %loc)
        except PermissionError:
            print("        Cannot Overwrite File, because it is being used by another program")
    elif ans == '2':
        fURL = input("        Enter URL: ")
        try:
            m.download_url(fURL)
            loc = os.getcwd()
            print("        File downloaded to: %s" %loc)
        except PermissionError:
            print("        Cannot Overwrite File, because it is being used by another program")

def importfile():
    imURL = input("        Enter File URL to be Imported: ")
    m.import_public_url(imURL)
    folder_node = m.find('Documents')
    m.import_public_url(imURL, dest_node=folder_node)
    print("        Imported")

def rename():
    f = input("        Enter Name: ")
    file = m.find(f)
    if file == None:
        print("        No such file")
    else:
        rf = input("        Enter New Name: ")
        m.rename(file, rf)
        print("        Done!")

while True:
    os.system('cls')
    
    print("  ███╗   ███╗███████╗ ██████╗  █████╗    ███╗   ██╗███████╗")
    print("  ████╗ ████║██╔════╝██╔════╝ ██╔══██╗   ████╗  ██║╚══███╔╝")
    print("  ██╔████╔██║█████╗  ██║  ███╗███████║   ██╔██╗ ██║  ███╔╝ ")
    print("  ██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║   ██║╚██╗██║ ███╔╝  ")
    print("  ██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║██╗██║ ╚████║███████╗")
    print("  ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝")
    print("                                                           ")
    print("                                             -by imshawan ")
    print("")                                                                 

    print("        1. Get user details")
    print("        2. Get account balance (Pro accounts only)")
    print("        3. Get account disk quota")
    print("        4. Get account storage space")
    print("        5. Get account files/folders")
    print("        6. Upload a file, and get its public link")
    print("        7. Find a file or folder")
    print("        8. Download a file from URL or filename")
    print("        9. Import a file from URL")
    print("        10. Create a folder")
    print("        11. Rename a file or a folder")
    print("        12. EXIT \n")
    sel = input("        Enter Selection: ")
    print("")
    if sel == '1':
        get_details()
        ps = input("\n        Press any key to continue...")
    elif sel == '2':
        bal()
        ps = input("\n        Press any key to continue...")
    elif sel == '3':
        quota()
        ps = input("\n        Press any key to continue...")
    elif sel == '4':
        get_storageInfo()
        ps = input("\n        Press any key to continue...")
    elif sel == '5':
        get_filenames()
        ps = input("\n        Press any key to continue...")
    elif sel == '6':
        upload_file()
        ps = input("\n        Press any key to continue...")
    elif sel == '7':
        find_file_folder()
        ps = input("\n        Press any key to continue...")
    elif sel == '8':
        download()
        ps = input("\n        Press any key to continue...")
    elif sel == '9':
        importfile()
        ps = input("\n        Press any key to continue...")
    elif sel == '10':
        create_fol()
        ps = input("\n        Press any key to continue...")
    elif sel == '11':
        rename()
        ps = input("\n        Press any key to continue...")
    elif sel == '12':
        print("        Exiting...")
        sleep(1)
        sys.exit()
    else:
        print("        INVALID CHOICE!")
        ps = input("\n        Press any key to continue...")
        
    
    
    
