import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Configura onde os arquivos serão salvos
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Lista todos os arquivos da pasta uploads
    arquivos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('drive.html', arquivos=arquivos)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo encontrado", 400
    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "OK", 200

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Tem que ser 0.0.0.0 para aceitar conexões do Wi-Fi
    app.run(host='0.0.0.0', port=8000)