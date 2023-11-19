from flask import Flask, render_template, send_file
from nbconvert import HTMLExporter

app = Flask(__name__)

@app.route('/')
def render_notebook():
    with open('Mental_Health_in_Tech.ipynb', 'rb') as file:
        notebook, _ = HTMLExporter().from_file(file)
    return render_template('index.html', notebook=notebook)

@app.route('/download')
def download_notebook():
    return send_file('Mental_Health_in_Tech.ipynb', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
