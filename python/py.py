fhand = open('')
count = dict()

for line in fhand :
    line = line.rstrip()
    words= line.rsplit()
    for word in words :
        count[word] = count.get(word, 0) + 1
        
lst = list()
for key,val in count.items() :
    lst.append(val,key)
lst = sorted(lst)

for val,key in lst[:10] :
    print(key, val)
    
    
    
    
    
'''Read lines from sict and sort it in an list :
fhand = open('')
count = dict()

for line in fhand :
    line = line.rstrip()
    words= line.rsplit()
    for word in words :
        count[word] = count.get(word, 0) + 1
        
lst = list()
for key,val in count.items() :
    lst.append(val,key)
lst = sorted(lst)

for val,key in lst[:10] :
    print(key, val)'''