#!/apollo/env/SDETools/bin/python
#Just a little demo of chunking

my_list = [1,2,3,4,5,6,7,8,9]
k = 2
 
def chunk(seq, num):
    out = []
    last = 0.0
 
    while last < len(seq):
       out.append(seq[int(last):int(last + num)])
       last += num
    return out
 
print chunk(my_list,k)

