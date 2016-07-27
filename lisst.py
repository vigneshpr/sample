'''1. Write a Python program to sum all the items in a list.
li=[2,3,6,6,4,5,9,4]

li=(2,3,6,6,4,5,9,4)

print("sum:",map(lambda x:x+2,li))
print(li)

print("sum:",reduce(lambda x,y:x+y,li))'''

li=(2,3,6,6,4,5,9,4)
ls=[]

'''for x in input:
    if x not in output:
      output.append(x)
  return output'''

for x in li:
    if x not in ls:
      ls.append(x)
print(ls)