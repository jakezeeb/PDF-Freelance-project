#%%
from os import listdir
from os.path import isfile, join
mypath = 'PDFs'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(files)
#%%