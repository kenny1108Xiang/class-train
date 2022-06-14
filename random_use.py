import random as rd
import os
class random_use:
    
    def __init__(self, how_many, start, end):
        self.how_many = how_many
        self.start = start
        self.end = end
    
    def random_int(how_many, start, end):
        os.getcwd()
        os.mkdir("random file")
        os.chdir("./random file")
        random_data =  open("random data.txt","x")
        for i in range(how_many):
            print(rd.sample(range(start,end), 1),end=" ",file=random_data)