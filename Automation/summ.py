import glob,os,sys
from shutil import copy2

for inpfile in glob.glob("./*/*/*/inpfile.gjf"):
    func = inpfile.split("/")[1]
    basis = inpfile.split("/")[2]
    molec = inpfile.split("/")[3]
    print("func = %s; basis = %s; mol = %s" % (repr(func),repr(basis),repr(molec)))
    copy2(inpfile, "./%s--%s--%s.gjf" % (func,basis,molec))

