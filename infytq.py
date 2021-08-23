#ABCMeta=2
#class Shape(metaclass=ABCMeta):
#    def __init__(self):
#        print("I Am in INIt")#

#    def draw_shape(self):
#        pass

#    def set_color(self):
#        pass

#class Circle(Shape):
#    def draw_shape(self):
#        print("Draw circle")

#a=Shape()


#x = input("Do you need the answer? (y/n): ")
#if x.lower() == "y":
#    required = True
#else:
#    required = False

    
#def the_answer(self, *args):              
#        return 42

    
#class EssentialAnswers(type):
    
#    def __init__(cls, clsname, superclasse ,a):
#        if required:
#            cls.the_answer = the_answer
                           


#class Philosopher1(metaclass=EssentialAnswers): 
#    pass


#class Philosopher2(metaclass=EssentialAnswers): 
#    pass


#class Philosopher3(metaclass=EssentialAnswers): 
#    pass
    
    
##plato = Philosopher1()
#print(plato.the_answer())





#class A(type):
#    def __init__(self,a,b,c):
#        self.kuch=2
#        print(f"{self.kuch}")

#class B(metaclass=A):
#    pass        
#x=B()



#myq1=Queue(3)
#myq2=Queue(3)
#for i in range(0,3):
#    myq1.enqueue


#class Singleton(type):
#    _instances = {}
#    def __call__(cls, *args, **kwargs):
#        print("cls instanece {cls._instances}")
##        if cls not in cls._instances:
 #           print(cls)
 #           print('A')
 ###       
   #         cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
   #     print(cls._instances[cls])
   #    return cls._instances[cls]
    
    
##class SingletonClass(metaclass=Singleton):
 #   pass


#class RegularClass():
#   pass


#x = SingletonClass()
#print(x)
#y = SingletonClass()
#print(y)
#print(x == y)


#x = RegularClass()
#print(x)
#y = RegularClass()
#print(y)
#print(x == y)
#True
#False


l=[]
l=[1,2]
a=list(filter( ,l))
print(a)