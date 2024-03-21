from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'upload' not in request.files:
        return redirect(request.url)
    file = request.files['upload']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the file or process it
        file.save(os.path.join('uploads', file.filename))
        return 'File uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
