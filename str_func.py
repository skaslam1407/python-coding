# ns = "kolkata"
# print(ns.upper())
# print(ns.lower())
# print(ns.capitalize())


#print(ns.index('z'))
#print(ns.find('x'))

# index() & find() both find index of thr sting but index() throw error 
# when string not find but find() not throw error instead return -1.


# print(ord('A'))
# print(ord('a'))

# print(chr(65))
# print(chr(97))

# np = 'welcome'
# print(np.isalpha())

# ss = '126sss'
# print(ss.isalnum())

# xx = '78889'
# print(xx.isnumeric())


#str = 'I love python and great language'
# str = 'I love {x} and {y} language'.format(x="LOVE",y="GREAT")
# print(str)

name = "Sekh"
age = 30

msg = "My name is {} and I am {} years old".format(name, age)
print(msg)
# Output: My name is Sekh and I am 30 years old

msg = "My name is {n} and I am {a} years old".format(n=name, a=age)
print(msg)
# Output: My name is Sekh and I am 30 years old


msg = f"My name is {name} and I am {age} years old"
print(msg)
# Output: My name is Sekh and I am 30 years old

print(f"Next year I will be {age + 1}")
# Output: Next year I will be 31

name = 'Rahul'
age = 23

msg = "My name is %s and I am %d years old" % (name, age)
print(msg)
# Output: My name is Sekh and I am 30 years old


#Use f-strings if you’re on Python 3.6+, since they are clean, fast, and readable.

pi = 3.14159265

print("Pi value: {:.2f}".format(pi))   # Using format()
print(f"Pi value: {pi:.2f}")           # Using f-string
# Output: Pi value: 3.14
