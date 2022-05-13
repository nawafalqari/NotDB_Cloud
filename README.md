# NotDB Cloud
An API to send or get data from **NotDB** databases on cloud

## Installation
#### PIP
```
pip install notdb-cloud
```

## Commands
```
> notdb-cloud --help
usage: notdb_cloud <command> [<args>]

NotDB Cloud command line tool v1.0.1

optional arguments:
  -h, --help          show this help message and exit
  -v, --version       Show the notdb_cloud version

Create or wipe or delete your db:
  Database commands

    create            Create a database
    secure            Delete an entire database
    wipe              Wipe a database documents out
    delete            Delete an entire database
    run               Run your databases server (important to connect to your dbs)
```

#### Create
Create a database
```
> notdb_cloud create
filename: [dbname]
```

#### Secure
Secure a database with a password
```
> notdb_cloud secure
filename: [dbname]
password: [password]
```

#### Wipe
Clear every document from the database
```
> notdb_cloud wipe
filename: [dbname]
```

#### Delete
Delete an entire database
```
> notdb_cloud delete
filename: [dbname]
```

#### Run
Run a webserver to connect with it to the database
```
> notdb_cloud run
Server PORT (default=5000): [port]
Do you want to get asked for db password once (y/n)? [y/n] # when trying to view a database data, you will be asked for the password, type "y" to get asked once

* Serving Flask app 'notdb_cloud.app' (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.       
Use a production WSGI server instead.
* Debug mode: off
* Running on all addresses.
WARNING: This is a development server. Do not use it in a production deployment.       
* Running on [URL]:[PORT] (Press CTRL+C to quit)
```

A URL will appere at the last line, you can use it followed by the database filename to connect to it

for example:
```
[IP]:[PORT]/test.ndb
```

### Databases On Replit
Fork the [Replit Template](https://replit.com/@nawafhq/NotDB-Cloud-Database-Template?v=1), follow the instructions in the README
![gif](./images/replit.gif)