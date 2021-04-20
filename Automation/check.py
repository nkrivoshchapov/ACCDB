import sys, os, glob

for file in glob.glob("./*.list"):
    lines = open(file, "r").readlines()
    for line in lines:
        xyzfile = "../Geometries/%s.xyz" % line.replace("\n","")
        if not os.path.exists(xyzfile):
            print(xyzfile.replace("../", ""))
