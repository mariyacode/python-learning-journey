# Dictionaries = key value pair
student = {'name': ' zera','age': 25 ,'courses': ['computer science','chemistry']}
print(student)
print(student['name'])
print(student.get('age'))
print(student.get('phone','Not found')) # the key is not in dictionary so not found output will recieve
student['name'] = 'joe' # name changed here from zera to joe
print(student)
student.update({'name':'joe' , 'age': 30 ,'phoneno': ' 568902345'})
print(student)
del student['age']  #deleted age
print(student)
age = student.pop('name') # already deleted age from there popped name
print(student)
print(len(student))
print(student.values()) # values only be printed
print(student.items())  #keys and values be printed
for key in student:
    print(key)


