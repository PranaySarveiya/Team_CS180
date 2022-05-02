import os

path = os.path.abspath(os.path.dirname(__file__))
path += "/backupCSV/"

files = os.listdir(path)
for file in files:
	file = file.split(".csv")[0]
	print(file)