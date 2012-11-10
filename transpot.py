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
            

@app.route('/translate/<filename>', methods=['GET'])
def translate(filename):
    
    filter = request.args.get('f')

    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if file_exists(file_path):
    
        po = polib.pofile(file_path)
        if filter == 'translated':
            po = po.translated_entries()
        elif filter == 'untranslated':
            po = po.untranslated_entries()
        elif filter == 'fuzzy':
            po = po.fuzzy_entries()
            
        valid_entries = [e for e in po if not e.obsolete]
        
        context = {
            'title': filename,
            'count': len(valid_entries),
            'entries': valid_entries,
            'filename': filename,
            'filter': filter
        }
        return render_template('editor.html', **context)
    else:
        flash('Ups!, you are looking for translation file that are not exists.', 'error')
        return redirect(url_for('home'))
    
    
if __name__ == '__main__':
    app.run()
