import argparse
import os
import pyonr
import notdb

def main():
   pass

def read(rel_path):
   import codecs
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

def get_filename():
   return input('filename: ')

def stabilize_file(_r:pyonr.Read):
   schema = {
      '__docs': []
   }
   fd = _r.readfile
   try:
      if not fd or not fd.get('__docs'):
         _r.write(schema)
   except AttributeError:
      _r.write(schema)

v = get_version('__init__.py')

if __name__ == '__main__' or __name__ == 'notdb_cloud.__main__':
   parser = argparse.ArgumentParser('NotDB Cloud', 'notdb_cloud <command> [<args>]', f'NotDB Cloud command line tool v{v}', argument_default=False)

   command_sub = parser.add_subparsers(dest='command', required=True, title='Create or wipe or delete your db', metavar='Database commands\n')
   command_sub.add_parser('create', help='Create a database')
   command_sub.add_parser('secure', help='Delete an entire database')
   command_sub.add_parser('wipe', help='Wipe a database documents out')
   command_sub.add_parser('delete', help='Delete an entire database')
   command_sub.add_parser('run', help='Run your databases server (important to connect to your dbs)')

   parser.add_argument('-v', '--version', action='version', version=f'notdb_cloud {v}', help='Show the notdb_cloud version')
   
   args = parser.parse_args()

   filename = get_filename()
   if args.command == 'create':
      notdb.create_db(filename)

   elif args.command == 'secure':
      file = pyonr.Read(filename)
      password = notdb.get_password()

      stabilize_file(file)
      filedata = file.readfile

      if filedata.get('__password'):
         raise ValueError('File already has password')

      filedata['__password'] = password
      file.write(filedata)

   elif args.command == 'wipe':
      file = pyonr.Read(filename)

      stabilize_file(file)
      filedata = file.readfile

      filedata['__docs'].clear()
      file.write(filedata)

   elif args.command == 'delete':
      os.remove(filename)

   elif args.command == 'run':
      pass