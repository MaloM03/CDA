from app import app

@app.route('/')
@app.route('/index')

def index():
    srtResult='ATTENTION TEST'
    return srtResult