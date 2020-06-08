print('print distinct list of elements along with their frequency of occurence\n Enter a list')
l=eval(input())
length=len(l)
fr=0
for x in l:
    count=0
    for y in l:
        if y==x:
            count+=1
    else:
         fr=(count/length)*100
         print('frequncy of element',x,'is',fr,'%')
input('enter press to exit')
