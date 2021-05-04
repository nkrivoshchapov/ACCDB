import sys,os,glob
from shutil import copy2
for file in glob.glob("./*log"):
    parts = file.replace("./","").replace(".log","").split("--")
    try:
        os.mkdir(parts[0])
    except:
        pass
    try:
        os.mkdir(parts[0]+"/"+parts[1])
    except:
        pass
    os.mkdir(parts[0]+"/"+parts[1]+"/"+parts[2])
    copy2(file, parts[0]+"/"+parts[1]+"/"+parts[2]+"/"+parts[2]+".out")
