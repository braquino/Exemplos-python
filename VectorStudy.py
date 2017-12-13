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
        except ZeroDivisionError:
            print("Cannot normalize a zero lenght vector")
        
    def dot_product(self, vector):
        return vector.x * self.x + vector.y * self.y + vector.z * self.z
    
    def angle(self, vector):
        return self.angle_rad(vector) / (math.pi / 180)

            
    def angle_rad(self, vector):
        try:     
            return math.acos(self.dot_product(vector)/(self.length()*vector.length()))
        except ZeroDivisionError:
            print("There is no existent angle")


vec_1a = Vector(7.887, 4.138)
vec_1b = Vector(-8.802, 6.776)

print(round(vec_1a.dot_product(vec_1b),3))

vec_2a = Vector(-5.955, -4.904, -1.874)
vec_2b = Vector(-4.496, -8.755, 7.103)

print(round(vec_2a.dot_product(vec_2b),3))

vec_3a = Vector(3.183, -7.627)
vec_3b = Vector(-2.668, 5.319)

print(round(vec_3a.angle_rad(vec_3b),3))

vec_4a = Vector(7.35, 0.221, 5.188)
vec_4b = Vector(2.751, 8.259, 3.985)

print(round(vec_4a.angle(vec_4b),3))

vec_ta = Vector(1, 2, -1)
vec_tb = Vector(3, 1, 0)

print(round(vec_ta.angle_rad(vec_tb),3))
