# PyDictFileEncy

A simple API used to encrypt the python dict into a file using AES256. The interaction is between the file and memory directly(No decrypted file.tmp will be created). The encrypted data is saved by string in a file on the disc. If one were developing a single thread app, this can be used as encrypted "SQL".
This API is a collection of the answers on StackOverflow.


## Install

```
pip install pydictfileency
```


## Usage
A (set of) python dict is collected in a "container" which will be operated directly.



## example and API

```
from pydictfileency import PyDictFileEncy
```




Create a container
```
#-----------------------------------------------------
# create a new filedict (with password = 'password')
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
# a file is created. One can check the context in it.
```



Connect to it (verify password)
```
#-----------------------------------------------------
# connect to a filedict
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
print(container.IsConnected())
# a filedict is connect. One can try another password.
```




Create a table (a table is a python dict)  
```
#-----------------------------------------------------
# create a table
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
container.CreateTableIfNotExist('testTable')
# remenber to save it
container.Save()
```


Show all tables
```
#-----------------------------------------------------
# get all the tables in container
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
# return a python dict 'dict_keys' type
l = container.GetTableList()
print(l)
```


Get a python dict in the container. One can have operations on it.
```
#-----------------------------------------------------
# get a normal python dict in the container so one can interact with it
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
d = container.GetTable('testTable')
print(type(d),d)
# ---  inser an element
d['new'] = 'hellow'
# remenber to save it
container.Save()
```

Remove a table
```
#-----------------------------------------------------
# remove a table
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
container.DropTable('testTable')
# remenber to save it
container.Save()
```




Reset a new password
```
#-----------------------------------------------------
# reset password
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
container.SetPassword('newpassword')
# remenber to save it
container.Save()
# the container itself is already renewed
print( container.IsConnected() )
```
