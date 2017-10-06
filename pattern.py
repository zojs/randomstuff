class Nizi:
    def SpremeniVzorec(a,b):
        ven=""
        i=0
        for c in b:
            if c==" ":
                ven+=" "
            else:
                ven+=a[i]
                i+=1
            if i==len(a):
                i=0
        return ven
a=input()
b=input()
print(Nizi.SpremeniVzorec(a,b))
