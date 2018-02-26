import random
times_t=[1,2,3]
already=set()
times=0
avg_sum=0
for i in range(100000):
    curtime=0
    already=set()
    while 1:
        st=random.randint(0,2)
        if (st not in already):
             #print(st)
             curtime+=times_t[st];
             already.add(st)
             if st==0:
                 break
    #print("out")
    avg_sum+=curtime
    times+=1
print("a)",avg_sum/times)

times_t=[1,2,3]
times=0
avg_sum=0
for i in range(1000000):
    curtime=0
    while 1:
        st=random.randint(0,2)
        curtime+=times_t[st];
        if st==0:
            break
    avg_sum+=curtime
    times+=1
print("b)",avg_sum/times)
