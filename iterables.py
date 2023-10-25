# Lists

def push_stack(list, element):
    list.append(element)
    return list

def pop_stack(list):
    element = list[-1]
    list.pop(len(list)-1)
    return list, element

def push_queue(list, element):
    list.append(element)
    return list

def pop_queue(list):
    element = list[0]
    list.pop(0)
    return list, element

if (__name__ == '__main__'):
    stack = []
    push_stack(stack, "ram")
    push_stack(stack, "raj")
    push_stack(stack, "rao")
    print(stack)
    stack, element = pop_stack(stack)
    print(element)
    print(stack)

    queue = []
    push_queue(queue, "sam")
    push_queue(queue, "som")
    push_queue(queue, "son")
    print(queue)
    queue, element = pop_queue(queue)
    print(element)
    print(queue)

#Creating tuples
#Using the tuple method
mytuple = tuple(('arul','bala',52,'male',60000,'arul'))
print(mytuple)
#From a list
list1 = ['arul','raj','ramesh']
mytuple1 = tuple(list1)
print(mytuple1)
#Just by assigning values
mytuple2 = ((2,4),(6,2),(3,5))
print(mytuple2)
#Using the count method
print('Count method - gives the number of occurrence ',mytuple.count('arul'))
#Using the index method
print('Index method - gives the position of the item',mytuple.index('male'))
#Getting the size of the tuple
print('len method - Tuple size ', len(mytuple))
#Accessing specific elements of a tuple
print('Accessing the last element ',mytuple[-1])
print('Accessing the first three elements ', mytuple[:3])
print('Accessing the elements after the 2nd ', mytuple[2:])
print('Accessing the 1st element of the 2nd set', mytuple2[1][0])

#Creating sets
#using the set method
myset = set(('raj','bala','annete',4))
print(myset)
#from another iterator
myset1 = set(mytuple)
print(myset1)
#by assigning values
myset2 = {(1,3),(3,5),(6,7)}
print(myset2)
myset.add('bala')
print(myset)
if 'bala' in myset:
    print('Element present')
for item in myset2:
    print(item)
myset3 = myset.union(myset1)
print('After the union ',myset3)
myset3.clear()
print('After clearing ',myset3)
myset = {1,2,3,4,5,6,7,8,9} 
myset2 = {2,4,6,8}
print('Is set1 a superset of set2', myset.issuperset(myset2))

# iterables share the same memory location
l1 = [2, 3, 4, 5]
l2 = l1
l2.append(6)
print(l1)

# Hetrogeneous Sort 
l1 = [3,5,2,'arul',6,'bala',8]
def mixed_sort(item):
    try:
        int(item)
        return(0,item)
    except:
        return(1,item)

print('Sorting a Hetrogeneous List ')
print('Original List ', l1)
l1.sort(key=mixed_sort,reverse=True)
print('Sorted List ', l1)
l1.append('Hello')
l2 = sorted(l1,key=mixed_sort)
print('Other sorted list using the Sorted built in function ', l2)

print('Sorting a list of tuples by the second value ')
l1 = [(2,3),(4,2),(5,1),(4,4)]
def sort_second(item):
    return item[1]
l2 = sorted(l1, key=sort_second)
print(l2)

l1 = [1,2,4,5,3]
print('The list', l1)
print('The first element l1[0] ', l1[0])
print('The last element l1[-1] ', l1[-1])
print('The last but one element l1[-2] ', l1[-2])
print('The first 3 elements l1[:3] ', l1[:3])
print('The last 3 elements l1[2:] ', l1[2:])
print('The sum of the list sum(l1) ', sum(l1))

t1 = (1,2,4,3,5,8)
t2 = sorted(t1)
print(t2)

# Reversing a list
print(l1)
l1.reverse()
print(l1)

# Reversing using 
print(l1[::-1])

# Creating a Dictionary
dict0 = {'brand':'Honda',
         'model':'City',
         'year':2004}
print('Entire Dictionary ', dict0)
print('Values of one Key ', dict0['brand'])
print('Items ', dict0.items())
print('Keys ', dict0.keys())
print('Values ', dict0.values())
dict0.update({'model':['City','Mobilio']})
print('Get value by providing key ', dict0.get('model'))
#Adding a new key value pair
dict0['color'] = 'Grey'
print(dict0)

# Using the zip command to tie together iterables
dict1 = {'name':['benhur','raj','ramesh','yuvi'],
         'age':[52,51,53,52],
         'city':['sfo','raleigh','columbo','chennai']}
list1 = list(dict1.values())
name_list = list1[0]
age_list = list1[1]
city_list = list1[2]
print(name_list)
print(age_list)
print(city_list)
list1 = zip(name_list,age_list,city_list)
print(list(list1))

dict2 = {'TN':'Tamil Nadu',
         'TS':'Telangana',
         'KA':'Karnataka',
         'DL':'Delhi',
         'CA':'California'
         }

print(dict2.get('TN'))
dict2.update({'TN':['Tamil Nadu','Tennesse']})
print(dict2)