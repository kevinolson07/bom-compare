from flask import Flask, render_template, request, redirect, url_for
from bom_compare import *
from io import TextIOWrapper


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=['POST','GET'])
def uploadFiles():
    if request.method == 'POST':
        # get the uploaded file
        uploaded_file = request.files['file']
        uploaded_file1 = request.files['file1']
        print("here")
        if uploaded_file.filename != '' and uploaded_file1.filename != '':
            print("Here")
            uploaded_file = TextIOWrapper(uploaded_file, encoding='utf-8')
            uploaded_file1 = TextIOWrapper(uploaded_file1, encoding='utf-8')
            old_bom, new_bom = selectBom(uploaded_file, uploaded_file1)
            desc = descChange(old_bom, new_bom)
            qty = qtyChange(old_bom, new_bom)
            rev = revChange(old_bom, new_bom)
            rmPart = removeParts(old_bom, new_bom)
            addPart = addParts(old_bom, new_bom)
            return render_template('results.html', len = len(rev), rev = rev, len1 = len(desc), desc = desc, len2 = len(qty), qty = qty, len3 = len(rmPart), rmPart = rmPart, len4 = len(addPart), addPart = addPart)

    return redirect(url_for('index'))




app.run(host='0.0.0.0', port=5000, debug=True)