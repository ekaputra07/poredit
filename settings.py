# Change this to False when used in production
DEBUG = True

SECRET_KEY = '\xc1l\x0bKs\x07*\xa4}\xbb=ba\xcdI\x0b]I\x9b\x00M\x0fD\xdb'

# Allowed file extension to upload, PO only of course 
ALLOWED_EXTENSIONS = ['po', 'pot']

# A directory where uploaded Po file will hosted
UPLOAD_FOLDER = '/home/eka/labs/translate/files/po'

# A directory where resulting Mo file will hosted
MO_RESULT_PATH = 'files/mo'

#SERVER_NAME = 'localhost:5000'
