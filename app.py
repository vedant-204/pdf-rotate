#rotate pdf pages flask
from flask import Flask, render_template, request, redirect, url_for, send_file
from PyPDF2 import PdfFileWriter, PdfFileReader
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
uploads_dir = 'upload' 

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(uploads_dir, 'original.pdf'))
        return redirect(url_for('rotate'))

@app.route('/rotate', methods = ['GET'])
def rotate():
    return render_template('rotate.html')

@app.route('/download', methods = ['POST'])
def download():
    if request.method == 'POST':
        pdf_in = open('upload/original.pdf', 'rb')
        pdf_reader = PdfFileReader(pdf_in)
        pdf_writer = PdfFileWriter()
        page_num = request.form['page_num']
        page = pdf_reader.getPage(int(page_num))
        angle = request.form['angle']
        page.rotateClockwise(int(angle))
        pdf_out = open('rotated/rotated.pdf', 'wb')
        pdf_writer.addPage(page)
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close() 
    return redirect(url_for('home'))
# @app.route('/rotate', methods=['POST'])
# def rotate():
    # if request.method == 'POST':
        # file = request.files['file']
        # file.save(os.path.join('static', file.filename))
        # pdf = PdfFileReader(os.path.join('static', file.filename))
        # pdf_writer = PdfFileWriter()
        # for page in range(pdf.getNumPages())ear
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