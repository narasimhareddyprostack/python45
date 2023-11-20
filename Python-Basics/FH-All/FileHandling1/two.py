#read data.txt file  and  write in new file bangalore.txt
fp1=open('data.txt','r+')

data=fp1.read()

fp2=open('bangalore.txt', 'w')
fp2.write(data)

fp2.close()
fp1.close()