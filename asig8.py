#Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
	def __init__(self, radius):
		self.r=radius
		
	def getArea(self):
		print(self.r*self.r*3.14)
		
	def getCircumference(self):
		print(self.r*2*3.14)
		
c =Circle(1)

c.getArea()
c.getCircumference()


#Create a Student Class and make Display And SetAge Method
class student:
	def __init__(self, name, rollno):
		self.n=name
		self.rn=rollno
	def show(self):
		print(self.n,self.rn)
	
s=student("serv",73)
s.show()
		
		
#Create a Temperature class. Make two Methods
class temperature:
	def __init__(self, celsius, fahrenheit):
		self.c=celsius
		self.f=fahrenheit
	def show(self):
		a=((self.c+32)*1.8)
		b=((self.f-32)/1.8)
		print(a)
		print(b)
t=temperature(10,20)
t.show()


#Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .

class movieDetails:
	def __init__(self, moviename, artistname, yearofrelease, ratings):
		self.mn=moviename
		self.at=artistname
		self.yr=yearofrelease
		self.r=ratings
	def display(self):
		print(self.mn,self.at,self.yr,self.r)
	def update(self, moviename, artistname, yearofrelease, ratings):
		self.mn=moviename
		self.at=artistname
		self.yr=yearofrelease
		self.r=ratings
m=movieDetails("holiday","akshay kumar","20-04-2015",5)
m.display()		
m.update("abc","def","20-04-2015",3)
m.display()

#Create a Expenditure class.And Initialize it
class expenditure:
	def __init__(self, expenditure, saving, totalsalary):
		self.ex=expenditure
		self.s=saving
		self.ts=totalsalary
	def display(self):
		print(self.ex,self.s)
		a=(self.ex+self.s)
		print(a)

		
c=expenditure(100,50,"a")
c.display() 
		
	

	
	
