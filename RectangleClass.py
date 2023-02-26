#Here is a possible implementation of the Rectangle class in Python:

#A constructor that creates a rectangle with the specified width and height. The default values are1 and 2 for the width and height, respectively.
#A method named getArea()that returns the area and a method named getPerimeter() that returns the perimeter of the rectangle.
#Write a test program that creates two Rectangle objects of width 3 and height 30 and the other with width 4.5 and height 45.5. The output should display the width, height, area, perimeter of each rectangle and the ratio by how much area one is larger than other.


#                         👇 SOLUTION DOWN HERE 👇

class Rectangle:
    def __init__(self, width=100, height=2): #these value are the one that will be used by default if we dont provide arguments later in the code, but if we provide arguments, these will be overwrited automaticaly (this is a good practice because we avoid errors in case there is not any argument provided 😇)
        self.width = width
        self.height = height
        #here we created a class and the parameters that gonna be used for each specific object once it is called 😃
    
    def getArea(self):
        return self.width * self.height
     #here we create a function that will be used further to calculate the area, using any given width and height in the object (like: rect1 = Rectangle(3, 30) )
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
     #here we've created a function to calculate te parameter using the parameter expression and using the width and the height (here we use self.width and self.height to specify that the value that will be provided will be representing the width only, which we created in our class and which will always be replaced with the arguent that we add in the object)
     
#To test the class, we can create two Rectangle objects with the specified dimensions, and print their properties and the ratio of their areas:

# Create two rectangles
rect1 = Rectangle(3, 30)
rect2 = Rectangle(4.5, 45.5)
#remember, these two are objects and in each of them we are using the class "Rectangle"

# Now we have to Print the properties of the rectangles and these are the new way to print values with string using the "format" function (i have to learn more about it to get it very well coz i like what am seeing here)
print("Rectangle 1: width = {}, height = {}, area = {}, perimeter = {}".format(rect1.width, rect1.height, rect1.getArea(), rect1.getPerimeter()))
print("Rectangle 2: width = {}, height = {}, area = {}, perimeter = {}".format(rect2.width, rect2.height, rect2.getArea(), rect2.getPerimeter()))

# now, let us calculate and print the ratio of the two areas using the dufferent values given
area_ratio = rect1.getArea() / rect2.getArea()
print("The area of Rectangle 1 is {:.2f} times larger than the area of Rectangle 2.".format(area_ratio))

