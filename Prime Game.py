from sys import stdin,stdout

max_num = 1000001
prime = [True]*max_num
prime[0]=prime[1]=False
count_list = [0,0]

def countPrime():
    count = 0
    for i in range(2,len(prime)):
        if prime[i]==True:
            count+=1
        count_list.append(count)

def genPrime():
    i = 2
    c = 2
    while i*i < max_num:
        if prime[i] == True:
            j = i*i
            while j < max_num:
                prime[j]=False
                j+=i
        i+=1
    return c

genPrime()
countPrime()

for _ in range(int(input())):
    x,y = map(int,stdin.readline().split())
    if count_list[x]<=y:
        stdout.write("Chef\n")
    else:
        stdout.write("Divyam\n")
