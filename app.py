from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from bom_compare import *

path = "/Users/cdsfkolson/Documents/Tether_device/Bom-Compare"
# app.config['UPLOAD_FOLDER']
# @app.route("/")
# def hello_world():
#     return render_template('index.html')


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      uploaded_file1 = request.files['file1']
      print("here")
      if uploaded_file.filename != '' and uploaded_file1.filename != '':
           print("Here")
           uploaded_file = "%s/%s"%(path, uploaded_file.filename)
           uploaded_file1 = "%s/%s"%(path, uploaded_file1.filename)
           print(uploaded_file, uploaded_file1)
           old_bom, new_bom = selectBom(uploaded_file, uploaded_file1)
           desc = descChange(old_bom, new_bom)
           qty = qtyChange(old_bom, new_bom)
           rev = revChange(old_bom, new_bom)
           rmPart = removeParts(old_bom, new_bom)
           addPart = addParts(old_bom, new_bom)
           return render_template('results.html', len = len(rev), rev = rev)
      return redirect(url_for('index'))

app.run(host='127.0.0.1', port=5000, debug=True)