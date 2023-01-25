from datetime import datetime
import os

# print all of the attributes and methods of os module.
# print(dir(os))

# print the current working directory
print(os.getcwd())

# change directory
os.chdir('C:/Users/Jitendra')
print(os.getcwd())

# list all the directories
print(os.listdir())

''' os.mkdir('test_1') creates a directory in the current directory.
    os. makedirs('test_1/test_2/test_3') goes deep down and creates all the directories in the given argument.
    for example we never created test_2 directory but this function will create that for us.
    similarly, os.rmdir('test_1) will remove the test_1 directory.
    os.removedirs('/test1/test2/test3/') will delete all the directories recursively within test1.
    Therefore always be careful while using os.removedirs('dir_name')
'''
os.mkdir('test_1')
print(os.getcwd())
os.rmdir('test_1')
os.chdir("C:/Users/Jitendra/git/practice_python")
print(os.listdir())
last_modification_time = os.stat('first.py').st_mtime
print(datetime.fromtimestamp(last_modification_time))

''' os.walk() gives a tuple of (string, list, list). Here the first 'string' is the path of the current directory,
    the second list is the list of directories in the current directory and the third 'list' is the list of all
    the files in the current directory.
'''

for path, dirs, files in os.walk("C:/Users/Jitendra/.cache"):
    print("Current Path: ", path)
    print("Sub-directories: ", dirs)
    print("Files: ", files)
    print()
