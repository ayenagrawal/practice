import os
import datetime
# print(os.getcwd())
# print(os.environ.get("PATH"))
os.chdir("C:/")

# this will make a directory
# os.mkdir("test_folder")

print(os.getcwd())
# print(os.listdir())

# this will print all files details of the files is the directiory passed as agrument

for a, b, c in os.walk("D:/python/"):
    print("Dir path :", a)
    print("Dir name :", b)
    print("File name :", c)
    print()

# this will show the creation time of a file
# flname = "test_folder"
# pt = os.stat(flname)
# crtime = (pt.st_ctime)
# print(flname, " is created on ", datetime.datetime.fromtimestamp(crtime))

# this will check a path/file exixts or not
# print(os.path.exists("C:/test_folder/"))
