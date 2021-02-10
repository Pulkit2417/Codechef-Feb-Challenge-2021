'''
for _ in range(int(input())):
    n = int(input())
    s = list(map(str, input().split()[:n]))
    count = 0
    for i in range(n-1):
        j=i+1
        while j<n:
            ft = s[i][0]+s[j][1:]
            st = s[j][0]+s[i][1:]
            #print(ft,st)
            if ft not in s and st not in s:
                count+=2
            j+=1
    print(count)
'''
'''
import math
for _ in range(int(input())):
    n = int(input())
    s = list(map(str, input().split()[:n]))
    countfc,countsco,i = 0,0,0
    fc = []
    sco = []
    while i<n:
        if s[i][0] not in fc:
            fc.append(s[i][0])
            countfc+=1
        if s[i][1:] not in sco:
            sco.append(s[i][1:])
            countsco+=1
        i+=1
    if countfc==1 or countsco==1:
        print(0)
    elif countfc>=countsco:
        print(countsco)
    elif countfc<countsco:
        print(countfc)
    print(countfc,countsco)
'''


for _ in range(int(input())):
    n = int(input())
    string_list = input().split()
    dictionary = {}
    count = 0
    for ele in string_list:
        sco = ele[1:]
        if sco in dictionary:
            print(sco)
            dictionary[sco].append(ele[0])
        else:
            dictionary[sco] = [ele[0]]
    nl = list(dictionary.keys())
    print(nl)
    for i in range(len(dictionary)):
        for j in range(i+1,len(dictionary)):
            b = len(set(dictionary[nl[i]]+dictionary[nl[j]]))
            print(b, dictionary)
            count+=(b-len(dictionary[nl[i]]))*(b-len(dictionary[nl[j]]))
    print(2*count)
