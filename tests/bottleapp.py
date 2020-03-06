import bottle
from bottle import route, run
from bottle.ext.pycouchdb import Plugin
from pycouchdb.exceptions import NotFound

couchdb = Plugin('mydb')
#couchdb = Plugin('mydb', 'http://username:password@localhost:5984')
app = bottle.Bottle()
app.install(couchdb)

@app.route('/')
def index():
    return 'Hello'

@app.route('/create/<_id>')
def create(_id, db):
    try:
        doc = db.get(_id)
    except NotFound:
        doc = db.save({'_id': _id})
    return doc

@app.route('/view/<_id>')
def view(_id, db):
    return db.get(_id)

if __name__ == '__main__':
    app.run(port=8000)
