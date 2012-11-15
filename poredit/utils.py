import os
import random

from flask import request, redirect, render_template
from flask import url_for, flash, send_from_directory
from werkzeug import secure_filename
import polib


def get_file_ext(filename):
    """ Get extension of a file """
    return filename.rsplit('.', 1)[1]
    
def allowed_file(filename, allowed_extension):
    """ Check if filename is allowed file type"""
    return '.' in filename and get_file_ext(filename) in allowed_extension

def generate_random_numbers(length):
    """Generate random number"""
    result = ''
    chars = '1234567890'
    for x in range(length):
        result += chars[random.randint(0, len(chars)-1)]
    return result
    
def file_exists(filename):
    return os.path.exists(filename)
    
def open_editor_form(app, request, filename):
    """ Display editor form """
    
    filter = request.args.get('f')

    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if file_exists(file_path):
    
        try:
            po = polib.pofile(file_path)
        except:
            flash('Invalid translation file detected.', 'error')
            return redirect(url_for('home'))
            
        percentage = po.percent_translated()
        
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
            'filter': filter,
            'percentage': percentage
        }
        return render_template('editor.html', **context)
    else:
        flash('Ups!, you are looking for translation file that are not exists.', 'error')
        return redirect(url_for('home'))


def save_translation(app, request, filename):
    """ Save the translations back to the file"""
    
    entries_count = request.form.get('count')
    filename = request.form.get('filename')
    
    if not entries_count or not filename:
        # If something wrong with the form
        flash('Invalid request!.', 'error')
        return redirect(url_for('home'))
    else:
        filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Open the file
        try:
            po = polib.pofile(file_path)
        except:
            flash('Invalid translation file detected.', 'error')
            return redirect(url_for('home'))
        
        for e in range(1, int(entries_count)+1):
        
            msgid = request.form.get('msgid_%s' % e)
            msgid_plural = request.form.get('msgid_plural_%s' % e)
            
            new_msgstr = request.form.get('msgstr_%s' % e)
            new_msgstr_plural = request.form.get('msgstr_plural_%s' % e)
            
            entry = po.find(msgid)
            # Set the new msgstr
            if entry:
                # In case there are Plural translation
                if msgid_plural:
                    msgstr_plural = {}
                    msgstr_plural[0] = new_msgstr
                    msgstr_plural[1] = new_msgstr_plural
                    setattr(entry, 'msgstr_plural', msgstr_plural)
                else:
                    setattr(entry, 'msgstr', new_msgstr)
                
        # Save the file
        po.save()
            
        flash('Translations saved.', 'success')
        return redirect(url_for('translate', filename=filename))
        

def download_po(app, request, filename):
    """ Download the po file """
    
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if file_exists(file_path):
        return send_from_directory(
                            app.config['UPLOAD_FOLDER'],
                            filename,
                            as_attachment=True)
        
    flash('You\'re trying to download file that are not exists.', 'error')
    return redirect(url_for('home'))
    

def download_mo(app, request, filename):
    """ Download the mo file"""
    
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if file_exists(file_path):
        try:
            po = polib.pofile(file_path)
        except:
            flash('Invalid translation file detected.', 'error')
            return redirect(url_for('home'))   
        
        # Now build the mo file
        mofilename = filename+'.mo'
        mopath = os.path.join(app.config['MO_RESULT_PATH'], mofilename)
        po.save_as_mofile(mopath)
        
        return send_from_directory(
                            app.config['MO_RESULT_PATH'],
                            mofilename,
                            as_attachment=True)
                            
    flash('You\'re trying to download file that are not exists.', 'error')
    return redirect(url_for('home'))
