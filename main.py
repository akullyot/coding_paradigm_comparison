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
        self.condition = condition.lower() 
        self.price = price
    #Purpose: Updates condition of the podracer to repaired
    def repaired(self):
        self.condition= "repaired"
 #Purpose: defines a podrace subclass with special boosting abilities       
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    def boost(self):
        self.max_speed = self.max_speed * 2
#Purpose: defines a podrace subclass with offensive abilities
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    def flame_jet(self, target_podracer):
        target_podracer.condition = 'trashed'

#Tests
if __name__ ==  "__main__":
    general_racer = Podracer(50, 'perfect', 500)
    general_racer.repaired()
    print(general_racer.condition)
    anakin_racer = AnakinsPod(30, 'repaired', 700)
    anakin_racer.boost()
    print(anakin_racer.max_speed)
    battle_racer = SebulbasPod(20, 'trashed', 900)
    battle_racer.flame_jet(anakin_racer)
    print(anakin_racer.condition)

