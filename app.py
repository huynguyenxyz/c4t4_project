from flask import *
from face import Face

import mlab
mlab.connect()
app=Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == 'GET':
        return render_template("calculation.html")
    elif request.method == "POST":
        form = request.form
        face_height = int(form['Chieu_dai_khuon_mat'])
        forehead_width = int(form['Do_rong_tran'])
        cheek = int(form['Do_rong_giua_2_ben_go_ma'])
        jawbone = int(form['Do_rong_xuong_ham'])
        def almost(a,b):
            if abs(a-b)<=2.5:
                return True
            else:
                return False
        face_cheek = almost(face_height,cheek)
        forehead_cheek = almost(forehead_width,cheek)
        forehead_jawbone = almost(forehead_width,jawbone)
        cheek_jawbone = almost(cheek,jawbone)
        if face_height>cheek>forehead_width>jawbone:
            face = "Diamond face"
        elif forehead_width>cheek>jawbone:
            face = "Heart face"
        elif face_height>max(forehead_width,cheek,jawbone)and forehead_cheek and forehead_jawbone and cheek_jawbone:
            face ="Long face"
        elif face_height>cheek and forehead_width>jawbone:
            face = "Oval face"
        elif min(face_height,cheek)>max(forehead_width,jawbone) and face_cheek  and forehead_jawbone:
            face = "Round face"
        elif face_cheek  and forehead_cheek and forehead_jawbone and cheek_jawbone:
            face = "Square face"
        elif jawbone>cheek>forehead_width:
            face ="Triangle face"
        else:
            face = 'x-men'
        if face == 'Diamond face':
            return render_template('diamond.html')
        elif face == 'Square face':
            return render_template('square.html')
        elif face == 'Heart face':
            return render_template('heart.html')
        elif face == 'Long face':
            return render_template('oblong.html')
        elif face == 'Round face':
            return render_template('round.html')
        elif face == 'Oval face':
            return render_template('oval.html')
        elif face == 'Triangle face':
            return render_template('triangle.html')
        else:
            print('error')
   
        
        







    

if __name__=='__main__':
    app.run(debug=True)