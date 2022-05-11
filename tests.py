import requests
from pyonr import loads
import notdb_cloud


# CONNNECT 👍 -> connect to db
# BRING    👍 -> bring data from db
# UPDATE   👍 -> update data
data = loads((requests.request('BRING', 'http://192.168.1.111:5000/t.ndb').content.decode('utf-8')))
print(data)

data['__docs'].append({'name': 'Mohammed'})

print(requests.request('UPDATE', 'http://192.168.1.111:5000/t.ndb', data={'update': f'{data}'}).content)

data = loads((requests.request('BRING', 'http://192.168.1.111:5000/t.ndb').content.decode('utf-8')))
print(data)

'''

python -c "exec('try: import notdb\nexcept ModuleNotFoundError: print("ni")')"

'''