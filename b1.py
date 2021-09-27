# 
# Vo Phuoc Nguyen - N17DCAT049
#
import random
#===================================== Bai tap cau 1: Random number
outfile =open ('solieu.txt','w')
# random so dong va so cot
row_col={"row":random.randint(2,10),"column":random.randint(2,10)}

#=== Tao so và ghi vao file
temp=[]
for j in range(0,row_col['row']):
	line=""
	temp.clear()
	for i in  range(0,row_col['column']):
		#random , chuyen thanh STRING va them vao list
		temp.append(str(random.randint(0,1000)))
	# Join lai bang dau cach
	line=" ".join(temp) 
	print(line)
	print(line,file=outfile)
print("Generated Done")
outfile.close()

#=== Doc file, cong va ghi vao file moi
infile =open ('solieu.txt','r')
outfile =open ('linetotal.txt','w')
array_in= []
for line in infile:
	array_in.clear()
	# Doc line trong file, xoa endline "\n", tach String dau " " ra thanh nhieu array
	array_in= line.rstrip().split(" ")
	sum=0
	for i in array_in:
		# Cong trong array lai...
		sum+= int(i)
	# Ghi ket qua ra file...
	print( "Dong"+str(array_in)+" co tong la: "+ str(sum),file=outfile) 
print("Processing Done")
infile.close()
outfile.close()

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

