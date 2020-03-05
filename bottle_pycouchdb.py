from bottle import PluginError
import pycouchdb
from pycouchdb.exceptions import NotFound
import inspect

class PyCouchDBPlugin:
    name = 'pycouchdb'
    api = 2

    def __init__(self, database, base_url=None, full_commit=True,
            authmethod='basic', verify=False, keyword='db'):
        self.database = database
        self.base_url = base_url or pycouchdb.client.DEFAULT_BASE_URL
        self.full_commit = full_commit
        self.authmethod = authmethod
        self.verify = verify
        self.keyword = keyword

    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, PyCouchDBPlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another pycouchdb plugin with "\
                        "conflicting settings (non-unique keyword).")

    def apply(self, callback, route):
        # get any overrides
        config = route.config.get('pycouchdb', {})
        database = config.get('database', self.database)
        base_url = config.get('base_url', self.base_url)
        full_commit = config.get('full_commit', self.full_commit)
        authmethod = config.get('authmethod', self.authmethod)
        verify = config.get('verify', self.verify)
        keyword = config.get('keyword', self.keyword)

        # do nothing if callback does not accept keyword
        callback_signature = inspect.signature(route.callback)
        if keyword not in callback_signature.parameters:
            return callback

        # wrap the callback
        def wrapper(*args, **kwargs):
            # connect to CouchDB
            server = pycouchdb.Server(base_url, full_commit=full_commit,
                    authmethod=authmethod, verify=verify)
            try:
                # connect to the database
                db = server.database(database)
            except NotFound:
                # create the database
                db = server.create(database)
            # make keyword available in the callback
            kwargs[keyword] = db
            return callback(*args, **kwargs)

        # return wrapped callback
        return wrapper

Plugin = PyCouchDBPlugin

