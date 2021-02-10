from itertools import combinations,chain
from sys import stdin,stdout
from operator import ixor
from functools import reduce

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()[:n]))
sum_list = [0]*(n+1)

def all_sum():
    sum_list[1] = sum(arr)%998244353
    i = 2
    xorsum = sum_list[1]
    while i<=n:
        comb = [*combinations(arr,i)]
        #print(comb)
        j = 0
        while j<len(comb):
            res = reduce(ixor,comb[j])
            #print(res)
            xorsum+=res
            j+=1
        sum_list[i]= xorsum%998244353
        i+=1

all_sum()
#print(sum_list)
for _ in range(int(stdin.readline())):
    stdout.write("%s\n" %sum_list[int(stdin.readline())])


