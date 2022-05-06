'''
NotDB Cloud
-----------

**NotDB Cloud** is an API that allows you to read and write data from your machine to a database on the cloud

    $ pip install notdb-cloud

Full documentation is avaliable on `Github <https://github.com/nawafalqari/NotDB_Cloud#readme>`_.
'''

from setuptools import setup, find_packages
import codecs
import os.path

# got these 2 functions from https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
   name='notdb_cloud',
   packages=find_packages(),
   include_package_data=True,
   install_requires=[
      'notdb>=1.0.2',
      'notdb-viewer>=1.2.4',
      'pyonr>=1.0.0',
      'bcrypt>=3.2.0',
      'flask',
      'flask-minify',
      'termcolor'
   ],
   version=get_version('notdb_cloud/__init__.py'),
   description='An API to send or get data from NotDB databases on cloud',
   long_description_content_type='text/x-rst',
   author='Nawaf Alqari',
   author_email='nawafalqari13@gmail.com',
   keywords=['notdb', 'db', 'database', 'notdatabsae', 'simple database'],
   long_description=__doc__,
   entry_points={
      'console_scripts': ['notdb_cloud=notdb_cloud.__main__:main']
   },
   license='MIT',
   zip_safe=False,
   url='https://github.com/nawafalqari/NotDB_Cloud/',
   project_urls={
      'Documentation': 'https://github.com/nawafalqari/NotDB_Cloud#readme',
      'Bug Tracker': 'https://github.com/nawafalqari/NotDB_Cloud/issues',
      'Source Code': 'https://github.com/nawafalqari/NotDB_Cloud/',
      'Discord': 'https://discord.gg/cpvynqk4XT',
      'Donate': 'https://paypal.me/NawafHAlqari'
   },
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Topic :: Database'
   ],
)