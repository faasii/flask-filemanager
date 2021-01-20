from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def get_files():
    dir_entries = scandir('storage/')
    dic = []
    fold = []
    for entry in dir_entries:
        
        ob = {}
            
        info = entry.stat()
        #print(info)
        #print(str(entry.name) + str(convert_date(info.st_mtime)))
        ob['size'] = str(round(info.st_size / 1024, 3))
        ob['name'] = entry.name
        ob['date'] = convert_date(info.st_mtime)
        ob['type'] = info.st_mode
        dic.append(ob)
               


get_files()    