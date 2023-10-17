#recreate FileNotFoundError and FileExistsError


#fp = open('rajni.txt', 'r')  #FileNotFound Error
fp = open('emp.txt','x')

fp.read()

fp.close()