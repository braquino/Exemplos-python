import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "X= " +str(round(self.x,3))+ ", Y= "+ str(round(self.y,3))+ ", Z= "+ str(round(self.z,3))
        
    def __add__(self, addend):
        ## The addend must be a vector, or a single number
        if type(addend) == Vector:
            return Vector(self.x + addend.x, self.y + addend.y, self.z + addend.z)
        else:
            return Vector(self.x + addend, self.y + addend, self.z + addend)
        
    def __sub__(self, subtrahend):
        ## The subtrahend must be a vector, or a single number
        return self.__add__(subtrahend * -1)
    
    def __mul__(self, product):
        ## The addend must be a vector, or a single number
        if type(product) == Vector:
            return Vector(self.x * product.x, self.y * product.y, self.z * product.z)
        else:
            return Vector(self.x * product, self.y * product, self.z * product)
        
    def length(self):
        return math.sqrt((self.x**2 + self.y**2 + self.z**2))
    
    def normalization(self):
        try:
            return self * (1/self.length())
        except:
            print("Cannot normalize a zero lenght vector")
        
    def dot_product(self, vector):
        return vector.x * self.x + vector.y * self.y + vector.z * self.z
    
    def angle(self, vector):
        return self.angle_rad(vector) / (math.pi / 180)

            
    def angle_rad(self, vector):
        try:     
            return math.acos(self.dot_product(vector)/(self.length()*vector.length()))
        except:
            print("There is no existent angle")
            
    def __eq__(self, other):
        try:
            return round(abs(self.x),5) == round(abs(other.x),5) and\
                round(abs(self.x),5) == round(abs(other.x),5) and\
                round(abs(self.x),5) == round(abs(other.x),5)
        except:
            print("Can´t compare distincts objects")
            
    def paralel(self, other):
        return self.normalization() == other.normalization()
            
    def projection(self, b):
        return b.normalization() * self.dot_product(b.normalization())
    
    def ort_to_base(self, other):
        return self - self.projection(other)
    
    def cross_product(self, other):
        x = self.y * other.z - other.y * self.z
        y = -(self.x * other.z - other.x * self.z)
        z = self.x * other.y - other.x * self.y
        return Vector(x, y, z)
    
    def orthogonal(self, other, tolerance=1e-10):
        return abs(self.dot_product(other)) < tolerance
    
    def paralelogram_area(self, other):
        return self.cross_product(other).length()
    
    def triangle_area(self, other):
        return self.paralelogram_area(other) / 2.0
    

a = Vector(8.462, 7.893, -8.187)
b = Vector(6.984, -5.975, 4.778)

print(a.cross_product(b))

a = Vector(-8.987, -9.838, 5.031)
b = Vector(-4.268, -1.861, -8.866)

print(round(a.paralelogram_area(b),3))

a = Vector(1.5, 9.547, 3.691)
b = Vector(-6.007, 0.124, 5.772)

print(round(a.triangle_area(b),3))


