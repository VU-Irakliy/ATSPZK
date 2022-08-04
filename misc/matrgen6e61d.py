import random
from os.path import exists

def idconv(k):
    if k < 26:
        return chr(k + 65)
    c = ""
    while k > 0:
        d = k % 26 + 64
        if (c == ""):
            d += 1
        c = chr(d) + c
        k //= 26
    return c

def genmatr(n):
    s = []
    c = []
    for i in range(n):
        c.append(idconv(i))
    s.append(c)
    for i in range(n):
        c = []
        for j in range(n):
            if (i != j):
                c.append(random.randint(1, 16))
            else:
                c.append(0)
        s.append(c)
    return s
        
def gluematr(z):
    r = []
    for w in z:
        s = ""
        for i in range(len(w)):
            if i > 0:
                s += "\t"
            s += str(w[i])
        s += "\n"
        r.append(s)
    return r

print("Enter matrix size: ")
n = int(input())
print('How many matrices? :')
lll = int(input())
om = 1
j = ""
for i in range(1 + om, lll + om+ 1):
    
    z = genmatr(n)
    r = gluematr(z)
    Flag = True
    while(Flag):
        # print("Enter file name: ")
        fn = 'matr' + str(i) + j + '.txt'
        # print(fn)
        if not exists(fn):
            # print('JOOOOOO')
            f = open(fn, "w")
            f.writelines(r)
            f.close()
            Flag = False
        else:
            print("File already exists!")
            print('Making with a new name')
            j += "a"