import os

print("Current working directory before: ", os.getcwd())

# TO change the current working directory os.chdir() method is used.
os.chdir('C:\\Users\\ewert\\Documents')

print("Current working directory after: ", os.getcwd())

# create directories
#os.mkdir()
#os.makedirs()
# Is neccessary to pass path var as argument of os.mkdir()
# directory = 'example'
# parent_dir = 'C:\\Users\\ewert\\Documents\\Python-'
# path = os.path.join(parent_dir,directory)
# os.mkdir(path)
# print(f"The dir was created {directory}")

# os.listdir() is used to get list of all files and directories in the specified directory
# print(os.listdir('/'))

# os.remove() is used to remove or delete a file path
# os.rmdir() is used to delete a empty directory

# os.rmdir('C:\\Users\\ewert\\Documents\\Python-\\example')

print(os.name)




