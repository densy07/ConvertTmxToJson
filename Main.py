
import subprocess
import string, os, sys
import random

tiledexe = r"C:\Program Files (x86)\Tiled\tiled.exe"
#tiledexe = r"cmd dir"

def ExportToJson (tmxFile, jsonFile):
    p = subprocess.Popen([tiledexe, '--export-map', tmxFile, jsonFile], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        out = p.stdout.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

tmxDir = os.getcwd() + os.sep + "tmx"
if os.path.exists(tmxDir) == False:
    print tmxDir + ' not exist'
    exit(1)

jsonDir = os.getcwd() + os.sep + "json" + str(random.randint(1000, 2000))
print jsonDir
if os.path.exists(jsonDir) == True:
    print jsonDir + ' exist'
    exit(1)

os.mkdir(jsonDir)

tmxList = os.listdir(tmxDir)
for tmxFile in tmxList:
    splits = os.path.splitext(tmxFile)
    if len(splits) != 2:
        continue

    ext = splits[-1]
    if ext != '.tmx':
        continue
    filename = splits[0]
    tmxFile = tmxDir + os.sep + tmxFile
    jsonFile = jsonDir + os.sep + filename + '.json'
    ExportToJson (tmxFile, jsonFile)

