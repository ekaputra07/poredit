import os
from flask import Flask, request, redirect, render_template
from flask import url_for, flash
from werkzeug import secure_filename
import polib

from utils import *

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Our homepage request handler
    """
    
    context = {
        'title': 'An online PO file editor and compiler',
        'page': 'home'
    }
    
    if request.method == 'GET':
        return render_template('home.html', **context)
    else:
        # If POST request
        file = request.files['pofile']
        if file and allowed_file(file.filename, app.config['ALLOWED_EXTENSIONS']):

            filename = secure_filename(file.filename)
            file_ext = get_file_ext(filename)
            
            po_id = generate_random_numbers(20)            
            filename = '%s.%s' % (po_id, file_ext)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('translate', filename=filename))
        else:
            flash('Invalid file extension. We only accept (.po, .pot) file!', 'error')
            return redirect(url_for('home'))
            

@app.route('/translate/<filename>/', methods=['GET', 'POST'])
def translate(filename):
    """
    File editing handler
    """
    
    if request.method == 'POST':
        return save_translation(app, request, filename)
    else:
        return open_editor_form(app, request, filename)
    

@app.route('/download/<filename>/', methods=['GET'])
def download(filename):
    """ File download handler """
    
    ftype = request.args.get('type')
    if ftype and ftype == 'mo':
        return download_mo(app, request, filename)
        
    return download_po(app, request, filename)
    
    
@app.route('/about/', methods=['GET'])
def about():
    context = {
        'title': 'About',
        'page': 'about'
    }
    return render_template('about.html', **context)
    

if __name__ == '__main__':
    app.run()
