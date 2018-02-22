NUMS= [i for i in range(-30,31)]
print (NUMS[:])
print('\n')

TUXAIOI=[]
import random
NUMS[0:60]
TUXAIOI = random.sample(NUMS,30)
print (TUXAIOI[:])
print('\n')

n = 0
for i in range (0,28):
    for j in range (1,29):
            if (TUXAIOI[i]+TUXAIOI[j]+TUXAIOI[j+1])==0:
                print (TUXAIOI[i],TUXAIOI[j],TUXAIOI[j+1])
                n = n + 1

if (n==0):
    print ("DEN YPARXOUN TETOIOI ARITHMOI")
