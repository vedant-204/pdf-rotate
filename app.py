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
        pdf_write = PdfFileWriter()
        page_num = request.form['page_num']
        angle = request.form['angle']
        for pagenum in range (pdf_reader.numPages):
            if pagenum != int(page_num):
                page = pdf_reader.getPage(pagenum)
                pdf_write.addPage(page)
            else:
                page = pdf_reader.getPage(int(page_num)-1).rotateClockwise(int(angle))
                pdf_write.addPage(page) 
        with open(r'rotated/rotated.pdf', 'wb') as fh:
            pdf_write.write(fh)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000 ,debug=True)
