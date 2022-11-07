#rotate pdf pages flask
from flask import Flask, render_template, request, redirect, url_for, send_file, save
from PyPDF2 import PdfFileReader, PdfFileWriter
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

# @app.route('/rotate', methods=['POST'])
# def rotate():
    # if request.method == 'POST':
        # file = request.files['file']
        # file.save(os.path.join('static', file.filename))
        # pdf = PdfFileReader(os.path.join('static', file.filename))
        # pdf_writer = PdfFileWriter()
        # for page in range(pdf.getNumPages()):
            # pdf_writer.addPage(pdf.getPage(page))
        # pdf_writer.addPage(pdf.getPage(0))
        # with open(os.path.join('static', file.filename), 'wb') as out:
            # pdf_writer.write(out)
        # return redirect(url_for('download', filename=file.filename))
# 
# @app.route('/download/<filename>')
# def download(filename):
    # return send_file(os.path.join('static', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000 ,debug=True)

# Path: index.html