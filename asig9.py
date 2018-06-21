#Perform Inheritance

# class Animal:
	# def animal_attribute(self):
		# print("animal")

# class tiger(Animal):
		# def animal_attribute(self):
			# print("tiger")


# a=tiger()
# a.animal_attribute()
			
			

#Write The Output of a Code


# class A:
    # def f(self):
        # return self.g()

    # def g(self):
        # return 'A'

# class B(A):
    # def g(self):
        # return 'B'

# a = A()
# b = B()
# print (a.f(),b.f())
# print (a.g(),b.g())


#output of Q2
#A B
#A B


#Create a Class Cope and Initialize it

# class cop:
	# def __init__(self,name,age,workexperience,desigination):
		# self.n=name
		# self.a=age
		# self.wx=workexperience
		# self.ds=desigination
	# def display(self):
		# print(self.n,self.a,self.wx,self.ds)
	# def update(self,name,age,workexperience,desigination):
		# self.n=name
		# self.a=age
		# self.wx=workexperience
		# self.ds=desigination
	
# class mission(cop):
	# def add_mission_details(self):
		# self.mission=input("Enter the mission:")
		# print(self.mission)
		
		
# s=mission("serv",20,"2year","officer")
# s.display()
# s.update("rudoff",20,"1year","hawaldar")
# s.display()
# s.add_mission_details()



#Create The Class Shape And Initialize It Initialize it

class shape:
	def __init__(self,length,breadth):
		self.l=length
		self.b=breadth
	def display(self):
		print(self.l,self.b)
		area=(self.l*self.b)
		print(area)
		
class square(shape):
	pass
		
class rectangle(shape):
	pass
	
s =square(3,9)
r =rectangle(4,8)
s.display()
r.display()





