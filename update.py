# Copyright (C) 2020 Dhruv Gera
# Copyright (C) 2020 xyzscape

import os
print("============================")
print("AncientOS Incremental Update")
print("============================")
print("Ver : xyz°inc.rev.0.1.alpha")
old_target=input("Old Path Target : ")
new_target=input("New Path Target : ")
print("Cok-ing . . .")
try:
		filecheck=open("generator.sh")
		filecheck.close()
except:
    code="./build/make/tools/releasetools/ota_from_target_files  --block -i old new incremental.zip"
    saveFile2=open("generator.sh",'w')
    saveFile2.write(str(code))
    saveFile2.close()
fin = open("generator.sh", "rt")
data = fin.read()
data = data.replace('old', old_target)
fin.close()
fin = open("generator.sh", "wt")
fin.write(data)
fin.close()
fin = open("generator.sh", "rt")
data = fin.read()
data = data.replace('new', new_target)
fin.close()
fin = open("generator.sh", "wt")
fin.write(data)
fin.close()
os.system("chmod a+x generator.sh")
os.system("bash generator.sh")
