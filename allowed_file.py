# This is a helper function for validating uploaded files
# First arg is name of file and the second is the extensions we are allowing
def allowed_file(filename, allowed_ext):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_ext