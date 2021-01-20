from flask import Flask , render_template, request,redirect,url_for
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from os import scandir

app = Flask(__name__)


UPLOAD_FOLDER = './storage'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





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
    print(dic)
            


    return dic



@app.route('/')
def index():
    dic = get_files()
    return render_template('index.html',dic=dic)

@app.route('/upload',methods = ['GET','POST'])
def file():
    if request.method == 'POST':
      f = request.files['file']
      filename = (secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      return redirect(url_for("index"))  




if __name__ == '__main__':
   app.run(debug=True)



#    filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             return hello()