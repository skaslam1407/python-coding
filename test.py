#print("hello world")

#a,b = map(int,(input("please enetr a number:").split(',')))
#c=a+b
#print("sum of %d and %d is : %d" % (a,b,c))

# a = 20 ; b = 7 
# if a > b :
#     print("a greater b")
# elif a == b:
#     print("a equal b")
# else:
#     print("Number not found")

#a = 5






# while(a < 10):
#     print("Number:",a)
#     a += 1

# for x in range(1,10,2):
#     print("number:",x)

# num = [4,5,7,3,9] 
# for i in num:
#     print(i)
#     i += 1     






class Person:
    def __init__(self, a):
        self.c = a
        print("Parent Constructor: " + str(self.c))

    def hello(self): 
        print("Hi I'm from Person")  


class Student(Person):
    def __init__(self, a):   # child constructor
        super().__init__(a)  # call parent constructor
        print("Child Constructor")

    def reading(self):
        print("I'm student") 


# create object of Student
s = Student(7) 
#s.reading() 
#s.hello()


#s.reading()
#s.hello()
       
       
 