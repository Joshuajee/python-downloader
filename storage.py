import os
from datetime import datetime as dt


try:
    os.mkdir("downloads")
except:
    pass

def storage(file, ext):
    date = dt.now()
    timestamp  = str(int(dt.timestamp(date)))
    f = open("downloads/download-"+ timestamp + "." + ext, "wb")
    f.write(file)
    f.close()
    