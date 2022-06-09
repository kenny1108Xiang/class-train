import random as rd

class random_use:
    
    def __init__(self, how_many, start, end):
        self.how_many = how_many
        self.start = start
        self.end = end
    
    def random_int(how_many, start, end):
        for i in range(how_many):
            print(rd.randint(start, end),end=" ")


