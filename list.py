from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def get_files():
    dir_entries = scandir('storage/')
    dic = []
   
    for entry in dir_entries:
        if entry.is_file():
            ob = {}
            info = entry.stat()
            print(entry.name)
            #print(str(entry.name) + str(convert_date(info.st_mtime)))
            ob['size'] = str(round(info.st_size / 1024, 3))
            ob['name'] = entry.name
            ob['date'] = convert_date(info.st_mtime)
            dic.append(ob)
            print(ob)
            #print(dic)

    print(dic)


get_files()            