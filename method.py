import re

handle=open('regex_sum_1624587.txt')
numlist=list()

for line in handle:
    line=line.rstrip()    
   # print(line)
    invalue=re.findall('[0-9]+', line)
   # print(invalue)
    
    
    if len(invalue) <1 :
        continue
        
    #print(invalue)
    for value in invalue:
       # print(value)
        value=int(value)
        #print(type(value))
        
        numlist.append(value)
#print(numlist)

sum=0
for num in numlist:
    sum=sum+num
print(sum)

#check if this line has pushed through


