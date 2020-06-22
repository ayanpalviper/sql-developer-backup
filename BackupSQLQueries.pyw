import os
import xmltodict as xml
import json
import datetime
import sys

src = 'D:/Worklog/VSCode/python/sql/'
p = 'D:/Worklog/Query Backup/'
entries = os.listdir(src)
if len(entries) == 0 :
    sys.exit()
x = datetime.datetime.now()
header = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
f = open(os.path.join(p, header + "-sql-history.txt"), "a")
for entry in entries :
    path = os.path.join(src, entry)
    log = open(path, "r").read()
    o = xml.parse(log)
    j = json.loads(json.dumps(o))
    x = j['history']['historyItem']['sql']
    f.write("\n")
    f.write("================================================================================================================================================================================================================================================================================================================================================")
    f.write("\n")
    f.write(x)
    os.remove(path)
f.close()
    
