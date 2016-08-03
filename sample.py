import random
s=[]		
for i in range(100):
	s.append(random.randint(0,100))
dic={}

for i in range(0,len(s),10):
	dic[i,i+10]=list(filter(lambda x:((x>=i)&(x<i+10)),s))

for k,v in dic.items():
    print(k)
    print(v)