import os
import shutil
fromdir = "assets"
todir = "dowloadedFiles"
lof = os.listdir(fromdir)
for i in lof:
    name, ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in ['.docx', '.pdf']:
        p1 = fromdir + "/" + i
        p2 = todir + "/" + "pics"
        p3 = todir + "/" + "pics" + "/" + i
        if os.path.exists(p2):
            print("moving" + i)
            shutil.copy(p1,p3)
        else:
            os.makedirs(p2)
            print("moving" + i)
            shutil.copy(p1,p3)