class person: 
    # __ is called as dunder 
    # 
    def __init__(self, name, age, m1, m2): # constructor 
        self.name = name
        self.age = age 
        self.m1 = m1
        self.m2 = m2

    def __del__(self): # destructor 
        print("object is being deleted")

    def __add__(self, other_object):
        return person(self.name,self.age, self.m1 + other_object.m1, self.m2 + other_object.m2)
    

        

# p = person('me', 25, 10, 20)
# q = person('sid', 25, 10, 20)
# r = p+q # adding two different objects is not possible, but you van specify __add__ and its functionality
#         # so that you can directly perform adding or any other operations 
#         # when you add two objects.
# print(r.name)
# print(r.m2)


#########################  decorators ####################

def mydecorator(function):
    def wrapper(*args, **kwargs):
        print('im a decorator')
        function(*args, **kwargs)
    return wrapper

@mydecorator
def hello_world(): # for now if we have params here, it doesnt wortk 
                    # because the wrapper doesnt have param, passing args, kwargs fixes this
    print('hellow world')

# hello_world()


#################### ex: logging ################
import time 
def logged(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        with open('logfile.txt', 'a+') as f: 
            fname = function.__name__
            f.write(f"{fname} returned the value {value} \n")
            f.write(f"{fname} took {after - before} sec to execute  \n")
    return wrapper
    
@logged
def add(x, y):
    for i in range(10000000):
        x += 10
    return x + y

# add(10, 20)

##################### generators ################ lazy execution 

def  mygenerator(n):
    for x in range(n):
        yield x ** 3

# values = mygenerator(9000000)

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

############### annotations #########

class person: 
    def __init__(self, name, age, gender): 
        # private attributes __ 
        self.__name = name
        self.__age = age # person.age doesnt going to work 
        self.__gender = gender

    # create properties to allow acess tot the attributes 
    @property
    def Name(self):
        return self.__name 
    
     # if this line is removed it throws an error
                 # because python doesnt have method overloading.
                 # we can not specify method with same name with diff attri
                 # this works in java and c butnot python, thus we need name.setter
    @Name.setter
    def Name(self, value):
        self.__name = value # this is a simple setter, we can have a complex 
                            # setter to assign a value to the private variable 

p1= person('sid', 25, 'M')
print(p1.Name) # no diorect access to tthe variable, access thorugh only property 


