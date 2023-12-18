#-----------------------------------------------------------------------Functional Paradigm -----------------------------------------------------------------------------------

#Purpose: flattens and sorts an array of integers in ascending order
#input:
def flatten_sort(input_list):
    pass

#Questions


#-----------------------------------------------------------------------OOP Paradigm -----------------------------------------------------------------------------------

#Purpose: Describes the methods and parameters associated with the podracers class
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        #lets do some standardization
        condition_options = ['perfect', 'trashed', 'repaired']
        assert condition.lower() in condition_options, "Please only use the three accepted condition descriptors: perfect, trashed, repaired"
        self.condition = condition 
        self.price = price
    #Purpose: Updates condition of the podracer to repaired
    def repaired(self):
        self.condition= "repaired"