# bottle-pycouchdb

Add support for [CouchDB](https://couchdb.apache.org/) to [Bottle](https://bottlepy.org/) using [pycouchdb](https://github.com/histrio/py-couchdb).

```python
import bottle
from bottle import route, run
from bottle.ext import pycouchdb

couchdb = pycouchdb.Plugin('mydb')
bottle.install(couchdb)

@route('/view/<_id>')
def view(_id, db):
    return db.get(_id)

run(host='localhost', port=8080, debug=True, reloader=True)
```
