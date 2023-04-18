class Teachers:
      def __init__(self,name,number,course_unit):
         #this __init__ is the method that is called when ever we create an object
         #  it is the one that python is looking for whenever we call an object
         self.name=name
         self.number=number
         self.course_unit=course_unit


teacher7=Teachers()      
teacher1=Teachers("martin","Data structure")
teacher1=Teachers("john","COA")
teacher1=Teachers("simon","LAN")
teacher1=Teachers("jake","NT")
