fruits=['apple','orange','kiwi','dragon fruit','banana']
fruits.pop()  # pop default as last element
print(fruits)
popped = fruits.pop()  # to view the popped element
print(popped)
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
num = [1,20,67,84,5]
num.sort()   # In default ascending order
print(num)
num.reverse()
print(num)
num.sort(reverse=True)  #descending order
print(num)
sorted(fruits) # will not sort it returns the original version
print(fruits)
sorted_fruits = sorted(fruits)
print(sorted_fruits)
sorted_num = sorted(num)
print(sorted_num)
print(min(num))
print(max(num))
print(sum(num))
mnc =['amazon','accenture','google','tcs','ibm','Infosys','jpmorgan']
print(mnc.index('Infosys'))
print('deloitte'in mnc)  # checking if deloitte is present in the list or not
print('amazon' in mnc)  # it gives true
for index,item in enumerate (mnc):  # they lists items one by one with index value
    print(index,item)
for index,item in enumerate (mnc,start = 1):  # starting index will be here 1
    print(index,item)
mnc =['amazon','accenture','google','tcs','ibm','Infosys','jpmorgan']
mnc_str = ','.join(mnc) # to get a string seperated by commas
print(mnc_str)
#Lists is mutable
#Tuple is immutable
#set
subjects = {'history','maths','physics','chemistry'}
print(subjects)
print('maths' in subjects)
subjects_2 = {'history','maths','arts','design'}
print(subjects.intersection(subjects_2))
print(subjects.union(subjects_2))
print(subjects.difference(subjects_2))
#empty lists
empty_list = []
empty_list = list()
#empty tuples
empty_tuple = ()
empty_tuple = tuple()
#set
empty_set = {}
empty_set = set()

