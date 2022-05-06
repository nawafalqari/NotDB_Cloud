'''
NotDB Cloud
-----------

NotDB Cloud is an API that allows you to read and write data from your machine to a database on the cloud

   $ pip install notdb-cloud

Full documentation is avaliable on [Github](https://github.com/nawafalqari/NotDB_Cloud#readme)
'''

from .app import is_secured

__version__ = '1.0.0b3'
__all__ = ['is_secured']