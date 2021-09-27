# 
# Vo Phuoc Nguyen - N17DCAT049
#
import random
#===================================== Bai tap cau 1: Random number
outfile =open ('solieu.txt','w')
row_col={"row":4,"column":5}

#=== Ghi file
temp=[]
for j in range(0,row_col['row']):
	line=""
	temp.clear()
	for i in  range(0,row_col['column']):
		temp.append(str(random.randint(0,100)))
	line=" ".join(temp)
	print(line)
	print(line,file=outfile)
print("Writting DONE")
outfile.close()

#=== Doc file
infile =open ('solieu.txt','r')
array_in= []
for line in infile:
	array_in.clear()
	array_in= line.rstrip().split(" ")
	sum=0
	for i in array_in:
		sum+= int(i)
	print( "Dong"+str(array_in)+" co tong la: "+ str(sum)) 
print("Done")
infile.close()

#===


#===================================== Bai mau 1
infile =open ('file.txt','r')
outfile =open ('new.txt','w')
for line in infile:
	print(line , file=outfile)
print("Done")
infile.close()
outfile.close()

#===================================== Bai mau 2 
BufferSize = 5000000
infile =open ('home.jpg','rb')
outfile =open ('newimageofHome.jpg','wb')
buffer = infile.read(BufferSize)
while len(buffer):
	outfile.write(buffer)
	print("It is copying an image, it might take some time... please wait...",end='')
	buffer = infile.read(BufferSize)
print()
print("Copying Done")
infile.close()
outfile.close()

