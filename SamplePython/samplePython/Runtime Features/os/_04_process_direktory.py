import os

print 'Starting:', os.getcwd()  #get current working directory 
print 'Moving up one:', os.pardir #naik satu tingkat dari CWD
os.chdir(os.pardir)  #change current working directory path
print 'After move:', os.getcwd()