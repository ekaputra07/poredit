# Change this to False when used in production
DEBUG = True

SECRET_KEY = 'your-super-secret-key-here'

# Allowed file extension to upload, PO only of course 
ALLOWED_EXTENSIONS = ['po', 'pot']

# A directory where uploaded Po file will hosted (absolute path)
# example: '/home/eka/poredit/files/po'
UPLOAD_FOLDER = '/home/eka/labs/translate/files/po'

# A directory where resulting Mo file will hosted (absolute path)
# example: '/home/eka/poredit/files/mo'
MO_RESULT_PATH = '/home/eka/labs/translate/files/mo'

#SERVER_NAME = 'localhost:5000'
