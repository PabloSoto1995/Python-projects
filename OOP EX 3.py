class Square():
    
    #square_list = []
    
    def __init__(self, s1):
        self.length = int(s1)
    
    # def __init__(self,s1):
    #     self.s1 = s1
    #     #self.square_list.append(self.s1)
    
    
    def change_size(self, number):
        self.length = (self.length) + number
        return self.length
        
    
    def calculate_perimeter(self):
        return (self.length)*4
    
    def print_perimeter(self):
        return("""{} by {} by {} by {}""".format(self.length, self.length, self.length, self.length))
    
    
    
square_1 = Square(2)
square_12 = square_1
square_2 = Square(4)
square_3 = Square(5)
#print(square_3.square_list)
print(square_3.print_perimeter())


def same(ob1, ob2):
    return ob1 is ob2

#print(same(square_1, square_2))
