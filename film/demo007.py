num=0
for i in range(2,200):
    k=True
    for j in range(2,i):
        if(i%j ==0):
            k=False
            break
    if(k==True):
        print("%d"%i)
        num = num+1
print("100-200之间的素数个数是%d"%num)


for i in range(1,10,1):
    for j in range(1,i+1,1):
        print(j,'*',i,'=',i*j,sep='',end='\t')
    print()
i = 1
sum=0
for i in range(1,101):
    if(i%2==1):
        continue
    sum+=i
print("1-100之间的偶数之和为%d"%sum)

for i in range(0,200,-1):
    if i % 17 ==0:
        break
print('200以内能被17整除的数中最大的是：',i)