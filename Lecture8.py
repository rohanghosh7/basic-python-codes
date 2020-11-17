#Dictionary
d = {'Rohan' : 90 , 'Ajay' : 86 , 'Rahul' : 100 , 'Aman' : 67}
print(d)

#Key
l = d.keys()
print(l)

#Value
b = d.values()
print(b)

#Delete
del d['Aman']
print(d)

#Update value
d['Rahul'] = 60
print(d)

#Append
d['Shreya'] = 78
print(d)

marks = d['Rohan']
print(marks)

#Search
if('Rahul' in d) :
	print("Yes")
else:
	print('No')

#Length
print(len(d))

#For loop
for i in d:
	print(i,d[i])

#Store list
n = {1 : [1,2,3] , 2 : [4,5,6]}
print(n)

#Return the list of values of dictionary in sorted order.

value_list = sorted(d.values())
print(value_list)

#Return the list of keys of dictionary in sorted order.

key_list = sorted(d.keys())
print(key_list)
