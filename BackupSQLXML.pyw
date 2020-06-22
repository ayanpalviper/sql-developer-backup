import os
import shutil
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def fileExists(dest, hash):
    dest_files = os.listdir(dest)
    for file_name in dest_files:
        thisHash = md5(os.path.join(dest, file_name))
        if(thisHash == hash):
            return True
    return False

backup = 'D:/Worklog/VSCode/python/backup/'
dest = 'D:/Worklog/VSCode/python/sql/'
src = 'C:/Users/pal/AppData/Roaming/SQL Developer/SqlHistory/'
src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        if fileExists(backup, md5(full_file_name)) == False :
            shutil.copy(full_file_name, dest)
            shutil.copy(full_file_name, backup)