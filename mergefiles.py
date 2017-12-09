# merge files
import datetime
fname=datetime.datetime.now()
fname=fname.strftime("env2/bin/"+str(fname)+".txt")
ls=[1,2,3]
for i in ls:
    files1=open("env2/bin/file"+str(i)+".txt",'r')
    content=files1.readline()
    print(content)
   
   
    files2=open(fname,"a")
    
    files2.write(content+"\n")
    files1.close()