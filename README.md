# bottle-pycouchdb

Add support for [CouchDB](https://couchdb.apache.org/) to [Bottle](https://bottlepy.org/) using [pycouchdb](https://github.com/histrio/py-couchdb).

```python
import bottle
from bottle import route, run
from bottle.ext.pycouchdb import Plugin

couchdb = Plugin('mydb')
#couchdb = Plugin('mydb', 'http://username:password@localhost:5984')
bottle.install(couchdb)

@route('/view/<_id>')
def view(_id, db):
    return db.get(_id)

run(host='localhost', port=8080, debug=True, reloader=True)
```
