from flask import Flask, render_template, abort, Response, request
import notdb
from notdb_viewer import viewer_html
import pyonr
from termcolor import colored

def refresh_data(file:pyonr.Read) -> dict:
   return file.readfile

def get_class(obj):
   return type(obj)

def get_obj_class_name(obj):
   return type(obj)().__class__.__name__

def is_secured(file:pyonr.Read):
   '''
   check if a NotDB database is secured with a password or not
   '''
   if file.readfile.get('__password'):
      return True
   return False

def create_app():
   
   app = Flask(__name__)

   @app.route('/', methods=['GET'])
   def index():
      return 'Home'

   @app.route('/<db_name>', methods=['GET', 'POST', 'BRING', 'UPDATE'])
   def db_viewer(db_name):
      try:
         file = pyonr.Read(db_name)
         db = None

         if request.method == 'POST':
            try:
               password = request.form.get('password', '')
               db = notdb.NotDBClient(db_name, password=password) 
               if app.take_password_once:
                  app.config[f'{db_name}_p'] = password
            except notdb.WrongPasswordError:
               return render_template('get_password.html', error='Password is wrong.', db=db_name)
         elif request.method == 'BRING':
            try:
               password = request.form.get('password', '')
               if is_secured(file):
                  db = notdb.NotDBClient(db_name, password=password)
               else:
                  db = notdb.NotDBClient(db_name)
               data = refresh_data(file)

               return f'{data}'
            except notdb.WrongPasswordError:
               err = 'Error: Invalid password'
               print(colored(f'\n{err}\n', 'red'))

               return f'{err}'
         
         elif request.method == 'UPDATE':
            try:
               password = request.form.get('password', '')
               if is_secured(file):
                  db = notdb.NotDBClient(db_name, password=password)
               else:
                  db = notdb.NotDBClient(db_name)
               
               update = request.form.get('update', None)
               if not update:
                  err = 'Error: Invalid update'
                  print(colored(f'\n{err}\n', 'red'))
               
                  return f'{err}'
                  
               file.write(update)
               return 'Success'

            except notdb.WrongPasswordError:
               err = 'Error: Invalid password'
               print(colored(f'\n{err}\n', 'red'))

               return f'{err}'

         else:
            if app.config.get(f'{db_name}_p', None):
               db = notdb.NotDBClient(db_name, app.config[f'{db_name}_p'])
            else:
               db = notdb.NotDBClient(db_name)

         data = refresh_data(file)

         db_info = {}

         db_info['Secured with password'] = True if data.get('__password') else False
         db_info['documents'] = db.documents

         return render_template('viewer.html',
                        documents=db.get({}),
                        db_info=db_info,
                        host=db.host,
                        get_obj_class_name=get_obj_class_name,
                        get_class=get_class,
                        f=file)
      except pyonr.FileExistsError:
         return abort(Response('Invalid db name'))
      except notdb.WrongPasswordError:
         return render_template('get_password.html', db=db_name)
      except Exception as err:
         print(err.__class__.__name__)
         return f'err'

   return app