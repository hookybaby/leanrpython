# coding: utf-8

# In[14]:

numbers = [2, 4, 5, 7, 9, 12, 14, 19]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

# In[19]:

for letter in 'Python':
    print('currnet letter :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('currnet fruit :', fruit)

print("Good bye!")

str = "google"
print(max(str))
