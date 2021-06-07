loop = [1,2,3]
for item in loop:
    print(item)

tuple = [(1,2), (3,4), (5,6)]
for a, b in tuple:
    print(a, b)

dict = {'k1':1, 'k2':2, 'k3':3}
for key, value in dict.items():
    print(key)

x = 1
while x < 5:
    print('this is True')
    x+=1
else:
    print('this is False')

word = 'hello'
for index, char in enumerate(word):
    print(index, char)

mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

# list comprehension serves as a forEach or .map (returns a new array of objects with logic performed on each)
celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5)* temp + 32) for temp in celcius]
conditional_fahrenheit = [( (9/5)* temp + 32) for temp in celcius if temp > 0]
print(fahrenheit)
print(conditional_fahrenheit)

def myfunc(*args):
    for item in args:
        print(item)
myfunc(40,10,20,30)

def random(**kwargs):
    print(kwargs)

print(random(shoe = 1,man = 2, wow = 'cat'))