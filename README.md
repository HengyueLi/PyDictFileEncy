# PyDictFileEncy

Store a python dictionary into a file with a password (by AES256). The interaction is between the file and memory directly(No decrypted file.tmp will be created). The encrypted data is saved by string in a file on the disc. One can load the data from a disc into a python dictionary and use it in the memory. The core part of this package is make use of the answer in [StackOverflow](https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256).




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

Get encrypted file (careful to use it): save the decrypted data into a file
```
#----------------------------------------------------
# password is also saved into the file!!!
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
container.SaveDecryptedDataToFile('DecryptedData.txt')
```


Read data from a decrypted file:
```
#----------------------------------------------------
# The current file will be overrided.
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
container.ReadDecryptedDataFile('DecryptedData.txt')
```

`SaveDecryptedDataToFile` and `ReadDecryptedDataFile` can be used to backup and restore.
