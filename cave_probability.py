import random
times_t=[1,2,3]
times=0
avg_sum=0
for i in range(10000000):
    curtime=0
    while 1:
        st=random.randint(0,2)
        curtime+=times_t[st];
        if st==0:
            break
    avg_sum+=curtime
    times+=1
print(avg_sum/times)
