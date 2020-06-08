print('print distinct list of elements along with their frequency of occurence\n Enter a list')
l=eval(input())
l1=l
length=len(l)
for x in l1:
    i=0
    count=0
    for y in l:
        if y==x:
            count+=1
            #l.pop(i)
            i+=1
            continue
    else:
        fr=(count/length)*100
        print('frequncy of element',x,'is',fr,'%')
        i+=1
        