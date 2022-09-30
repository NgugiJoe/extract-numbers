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
        
    print(invalue)