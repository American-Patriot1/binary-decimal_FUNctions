numm=255
def bin_to_num(num):
    rnum=0
    curant_num=1
    for i in range(len(num)):
        if (num[((i+1)*-1)])=="1":
            rnum+=curant_num
        curant_num=curant_num*2
    return rnum
def num_to_bin(num):
    cnum=128
    rnum=""
    for i in range(8):
        if num-cnum>=0:
            num=num-cnum
            rnum=rnum+"1"
        else:
            rnum=rnum+"0"
        cnum=cnum/2
    return(rnum)
print(num_to_bin(numm))