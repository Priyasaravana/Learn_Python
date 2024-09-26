class parentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def parentMethod(self):
        product_of_num = self.a * self.b
        return product_of_num
    
p_obj = parentClass(5, -9)
print('Product = ' , p_obj.parentMethod())


class childClass(parentClass):
    def __init__(self, x):
        parentClass.__init__(self, 5, -9)
        self.x  = x

    def childMethod(self):
        result = self.parentMethod() ** self.x
        return result
    
c_obj = childClass(2)
print('Answer = ', c_obj.childMethod())