print("usman tahir")
price=34.4
print(type(price))
a=32
b=34
print(a==b)
print(a != b)
num=10
num *=5
print(num)
#types of casting
A=str("23")
B=str(34)
print(A+B)

#input
"""value=float(input("enter the yuor name")) 
print(type(value))"""

"""num=float(input("enter yor number"))
num1=float(input("enter yor number"))
print("average is",(num+num1)/2)"""

#concateniation
str1="hello"
str2="words"
str_final=(str1+str2)
#lenght
print(len(str1))
print(len(str_final))
# index str[]
print(str1[0])
#slice index
print(str1[0:2])
#slice neg index
print(str2[-3:-1])

print(str1.endswith("o"))
print(str1.capitalize())
print(str_final.count("o"))
print(str1.replace("h","o"))

#if elif condition

light="blue"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light =="yellow"):
    print("wait")
else:
    print("run")


#age = int(input("Enter your age: "))
age=23
if age > 18:
    print("you can vote")
else:
    print("you cannot vote")

marks=33
if(marks>90):
    print("grade A")   
elif(marks>80 and marks<90):
    print("grade B")
elif(marks>70 and marks<80):
    print("grade C")
else:
    print("fail")
#nesting condition
age=51
if(age>=18):
    if(age<50):
        print("you can drive")
    else:
        print("you cannot drive")
else:
    print("pheli if condition false")

#example
'''a=int(input("enter the fist number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=int(input("enter the fourth number"))
if(a>b and a>b and a>c and a>d):
    print("fisrt number is greater")
elif(b>c and b>d):
    print("second number is greater")
elif(c>d):
    print("third number is greater")
else:
    print("forth number is greater")'''

 #list in python
marks=[12,32,14,12,23.34]
print(marks[1:3])
print(marks)
print(marks.sort())
print(marks)
marks1=marks.reverse()
print(marks1)

marks.copy()
print(marks)
#access the lsit
#print(marks[3])
#marks[3]="uzair"

#slice of list

#list method
print(marks.append(2))

print(marks)
print(marks[2])
print(type(marks))
#tuple immutable
tuple=("usman","tahir","uzair",21)
print(tuple)
print(type(tuple))
print(tuple[0])
#slice
print(tuple[0:2])
#index
print(tuple.index("usman"))
print(tuple.count(21))

#question
'''movie=[]
movie.append(input("enter the name of movie"))
movie.append(input("enter the name of movie"))
movie.append(input("enter the name of movie"))
print(movie)'''

#dictionary
information={
    "name":"usman",
    "age":21,
    "subject":["python","c++","java"],
    "tuple":("typle are same as the list"),
    "gpa":3.12,
}
print(type(information))
print(information["age"])
information["surname"]="tahir"
print(information["gpa"])

#nested dictionary
student={
    "name":"usman",
    "age":21,
    "subject":{
        "phy":21,
        "chem":21,
    }
}
#student["phy"]=87
print(student)
#dictionary method
print(list(student.keys()))

#acess all the key values
print(student.values())
print(student.items())

print(student.get("age"))
#set ignore the duplicate value and unorder list set are mutable but set element are immutable
collection={1,2,3,4,"words",4}
collection.add(5)
collection.remove(4)
print(collection)

print(type(collection))
print(len(collection))
#emty set
collection=set()
print(type(collection))
#intersection method of set
set1={1,2,3,4}
set={1,3,5,6}
print(set1.intersection(set))

#while loop
'''i=1
while i<=5:
    print("hello",i)
    i+=1      #i=i+1

#reverse while loop
i=5
while i>=1:
    print(i)
    i-=1'''

    #question print table
 
'''n=int(input("enter the number"))
i=1
while i<=10:
    print(n*i)
    i+=1'''
#question 4
num=[1,2,3,43,21,34,111,12]
index=1
while index<len(num):
    print(num[index])
    index+=1

#break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i +=1
    #continues
i=1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
#for loop in python
list=[1,2,3,4,5]
for values in list:
    print(values)

str="usman tahir"
for char in str:
    if(char == 'a'):
        break
    print(char)
else:
    print("end loop")
num=(11,22,33,44,55,66,77)
x=55

for values in num:
    if(values==x):
        print(values)
#range
for i in range(2,10):
    print(i)     
#range function for loop
for i in range(2,10,2):#start, stop ,step
       print(i)
#n mutlinumber range
'''n=int(input("enter the number"))
for i in range(1,11,3):
    print(n*i)'''


#function block of statment that perform specfic task

def calcu_sum(a,b):#parameter means function take input
    sum=a+b
    print(a+b)
    return sum   
calcu_sum(1,4)#arugment 
calcu_sum(33,22)

#function define
def calcu_multi(a,b):
    return a*b
multiply=calcu_multi(11,2)
print(multiply)

#calucalate average of 3 number

def avg(a,b,c):
    avg=(a+b+c)/3
    
    return avg
output=avg(2,3,55)
print(output)

#recursion
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)    
def fact(n):
    if(n==1):
        return 1
    return fact(n-1) * n
print(fact(5))

#file input and output

#read
f=open(r"G:\Usman\python code\demo.txt","r")
data=f.read()
print(data)

#write means overwrite and add new line
f=open(r"G:\Usman\python code\demo.txt","w")
data=f.write("I am student of software engineering")
print(data)

#readline
f=open(r"G:\Usman\python code\demo.txt","r")
data1=f.readline()
print(data1)

#write+
f=open(r"G:\Usman\python code\demo.txt","w+")
data=f.write("my name is usman tahir")
print(data)

#read+
f=open(r"G:\Usman\python code\demo.txt","r+")
data=f.read()
print(data)
f.close()

#append last py
f=open(r"G:\Usman\python code\demo.txt","a+")
data=f.write("my father name is tahir")
print(data)

#with open syntex
with open(r"G:\Usman\python code\demo.txt","r") as f:
    data=f.read()
    data=data.replace("my","i")
    print(data)
    
  
with open(r"G:\Usman\python code\demo.txt","w") as f:
    f.write(data)

#oop in python
#class and object
class student:
    age = 23
    name = "uzair rana"

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("student data store in database")

    def hello(self):
        print("function is create in oop", self.name)

    def get_marks(self):       
        return self.marks

    @staticmethod
    def hello():
        print("static method")
s1 = student("usman tahir", 67)
s1.hello()
print(s1.get_marks())   
print(s1.age)

#abstraction
class car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clucth=False
    def start(self):
        self.clucth=True
        self.acc=True
        print("car is started")
car1=car()
car1.start() 

#private method
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        #self.__acc_pass=acc_pass

acc1=account(5264,10983)
print(acc1.acc_no)
#print(acc1.__acc_pass)
 
#inheritance in oop
class car():
    @staticmethod
    def start():
        print("car is start")
    @staticmethod    
    def stop():
        print("car is stop")
class toyotacar(car):
    def __init__(self,name):
        self.name=name

car1=toyotacar("grandi")
print(car1.name)

class student:
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
    @property
    def percantage(self):
        return str((self.phy+self.math+self.chem)/3) + "%"          
st1=student(77,45,88)
print(st1.percantage)
st1.phy=88
print(st1.p)

def avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
result=avg(1,2,44)  
print(result*10)  

  
def calu(a,b,c):
    add=a+b+c
    print(add)
    
calu(1,2,2)  
       
  