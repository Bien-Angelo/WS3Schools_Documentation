#!/usr/bin/env python3

#Multi line String
a = '''Beauty is in the eye of the Beholder,
yet when the Beholder beholds beauty,
what beauty is there to behold?'''

print(a)


b = 'Hello, World!'

# An example of strings as arrays with 0 being the start
print(b[0])

# Looping String that prints each letter until the word banana is spelt
for c in 'banana':
	print (c)

'''
Checking for certain phrases or characters 
if present in the string, returns a boolean
value
'''
txt = 'The best things in life are free!'

print ('free' in txt)
print ('none' in txt)

if 'free' in txt:
	print("Yes, 'free' is present!")

if 'expensive' not in txt:
	print("No, 'expensive' is NOT present!")
