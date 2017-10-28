import os, sys, glob

# Usage : to rename with certain keywords in all pdf

# Command to run :
# python3 rename.py <dir location> 

os.system("clear")
path = sys.argv[-1]
appendWord = "WS_"
extn = "PDF"
print("append word ::",appendWord)
print("dirPath ::",path)
files = glob.glob(path+'*.'+extn)
for file in files:
    splits = file.split("/")
    filename = splits[len(splits)-1]
    os.rename(path+filename, path+appendWord+splits[len(splits)-1])

print("Success")
