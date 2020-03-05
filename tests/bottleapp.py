import bottle
from bottle import route, run
from bottle.ext import pycouchdb

couchdb = pycouchdb.Plugin('mydb')
app = bottle.Bottle()
app.install(couchdb)

@app.route('/view/<_id>')
def view(_id, db):
    return db.get(_id)

if __name__ == '__main__':
    app.run()
