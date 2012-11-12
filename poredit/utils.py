import os
import random

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
