from setuptools import setup

setup(name='bottle-pycouchdb',
        version='0.1',
        description='Add support for CouchDB to Bottle using pycouchdb',
        url='https://github.com/carloshanson/bottle-pycouchdb',
        author='Carlos Hanson',
        author_email='carlos@clanhanson.com',
        license='MIT',
        py_modules=['bottle_pycouchdb'],
        install_requires=['bottle', 'pycouchdb'],
        zip_safe=False)
