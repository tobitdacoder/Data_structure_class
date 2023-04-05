class Teachers:
      def __init__(self,name,course_unit):
         #this __init__ is the method that is called when ever we create an object
         #  it is the one that python is looking for whenever we call an object
         #self.name=name
         self.name=name
         self.course_unit=course_unit
         

print(type(Teachers))
''' this will run perfectly because, since we did not provide parameters, the init method used will be the default one from python'''

#teacher7=Teachers()      
Teacher1=Teachers("martin","Data structure")
Teacher2=Teachers("john","COA")
Teacher3=Teachers("simon","LAN")
Teacher4=Teachers("jake","NT")

