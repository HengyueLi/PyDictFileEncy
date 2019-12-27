from pydictfileency import PyDictFileEncy

#-----------------------------------------------------
# create a new filedict (with password = 'password')
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
# a file is created. One can check the context in it.


#-----------------------------------------------------
# connect to a filedict
container = PyDictFileEncy('encrypted.dat','password')
container.connect()
print(container.IsConnected())
# a filedict is connect. One can try another password.
