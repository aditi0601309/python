f1=open("input123.txt",mode='r')
f2=open("input1234.txt",mode='w')
shutil.copyfile("input123.txt",mode='w')
f2.write(f1.read())
shutil.copyfile("input123.txt","input1234.txt")
f1.close()
f2.close()
                
