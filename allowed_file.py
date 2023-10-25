# This is a helper function for validating uploaded files
# First arg is name of file and the second is the extensions we are allowing
ALLOWED_EXT = {'csv'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT