'''3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4=dict(dic3.items()+dic1.items()+dic2.items())
print(dic4)



dic11={1:10, 2:20} 
dic22={3:30, 4:40} 
dic33=dict(dic22.items()+dic11.items())
print(dic33)

