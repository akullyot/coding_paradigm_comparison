#-----------------------------------------------------------------------Functional Paradigm -----------------------------------------------------------------------------------

#Purpose: flattens and sorts a list of integers in ascending order
def flatten_sort(input_list):
    flat_list = []
    for element in input_list:
        if isinstance(element, list):
            flat_list.extend(flatten_sort(element))
        else:
            flat_list.append(element)
    #now finally sort the function and return it 
    return sorted(flat_list)
#Tests
if __name__ ==  "__main__":
    list_to_sort = [[3, 5,100],1, [7, 3, [2,3], 9], [1, 12]]
    print(flatten_sort(list_to_sort))

            

#Questions
#1. How does this solution ensure data immutability?
    """
        To ensure data immutability, you can never have any declared value change.  Instead, if you want to track a change to that value, you return it as a new variable.
        Here, you can see I ensured no side effects by not ever changing my list_to_sort variable value, but rather using the function flatten_sort to take that list_to_sort variable and use it to return my new variable
        (which here isnt actually given a declaration, but rather im just calling flatten_sort on list_to_sort and feeding it directly into the print function).
    """
#2.Is this solution a pure function? Why or why not?
    """
        Yes, this function is a pure function due to two reasons:
        First, it produces no side effects, so no states outside of the scope of the function are changed.
        Additionally, it only relies on the arguments inputted into the function. 
        Though it is worth noting we are using a few inbuilt methods/functions like sorted, append, etc. In the way that I am using them, I'm not producing any side effects nor are they going to ever return a different result for the same argument values.
        But I did have to be somewhat careful on what inbuilt methods I chose. For example, if I had used sort() versus sorted() here, it probably would still be a pure function but I get into a danger zone because sort() itself is an inpure function as it modifies its input directly. 
        Though, as you notice as well, using sort() versus sorted() still wouldnt produce any side effects outside the scope of the function or rely on arguments outside of the inputs fed into it, so I'm not actually sure if that would break this from being a pure function 
        in the way that I used it. If I did something like sort(input_list) at the beginning, it would definitely become an impure function. I would love to know the actual answer on if you use an impure function to make a pure function but it doesn't break the higher order function's "pureness"
        is it still pure.
    """
#3.Is this solution a higher order function? Why or why not?
    """
    This is not a higher order function because it does not take another function as an argument. 
    """
#4.Would it have been easier to solve this problem using a different programming style?
    """
        In this situation, I don't think it would be much easier to solve it using a different paradigm. Its pretty straightforward to flatten and sort a list (at least its straightforward when I can use inbuilt sorting algorithms and not have to worry about that!)

    """
#5.Why in particular is functional programming a helpful paradigm when solving this problem?








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

#Questions
#1.How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    #Encapsulation.
    #Abstraction
    #Inheritance
    #Polymorphism
#2.Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#3.How in particular did Object Oriented Programming assist in the solving of this problem?
    


#Overall Questions

#1.Is one of these coding paradigms "better" than the other? Why or why not?
    """
        Overall I feel this question is too large of one for me to actually answer at the time being and relies on a more rigorous understanding of the theory behind computer science, which I do not have. I tend 
        to think more theoretically than in practice when words like better are used, I tend to think of things like robustness and a language's ability to debug/"understand" itself (think at the level of Turing Tests). In that sense, to create an ideal language,
        its going to be easier to take a functional approach. I come from a system's biology background and literally the whole goal of my field is to keep abstracting down and down to find a minimal complete model. The ultimate goal of that would be to
        take the entirety of molecular biology and essentially decompose behaviors into a functional paradigm, where we have functions that rely on other functions to build up what is an incredibly complicated system of life. Which if you think about it, is literally just trying to use lambda calculus
        in probably one of the more ambitious goals of the 21st century. So I'm clearly biased to say at a theory level, functional programming is the ultimate manifestion of computer science.  So overall, if I had to say which enginnering paradigm best captures "the platonic Form" of computer science, 
        I would lean towards a functional paradigm. But I also don't understand enough about memory management and performance of the two different approaches to say which one is in practice the most efficient and assume since that is a question of practice versus theory, it is going to depending heavily on the use case.

        But that most definitely does not mean I'm about to whip out Haskell when I want to go make a basic CRUD application, or can you even imagine how hard reproducing a front end framework like React would be using only functional considerations? And on the flip side, it would be a repetitive, verbose nightmare probably rife with bugs that would be very hard to figure out if I tried to take some old 
        undergrad work I did in physics and convert that over to an OOP approach. So take this answer however you will. 
    """
#2.Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
    """
        As I alluded to above, it's going to entirely depend on the use case. But given the scope of this current class and what we are trying to accomplish, I would prefer an OOP approach. It makes a lot of sense when we have 

        But I also like languages like python and javascript that aren't rigorously either (and it's probably not a coincidence that those are the two languages we are using in this course), and you can kind of mix and match to produce the exact effects you want for whatever application you are developing. It's nice to take a functional approach to certain methods within classes if they are super data analytics heavy,
        but then just encapsulate that into the relevant class and not have to abstract it out to work with everything. I can see how this mixy matchy ness may make it harder to scale up and maintain and test as well, so maybe with more experience actually trying to do that I wouldn't like these more dynamic approaches, but for now it seems nice to use either when I see it necesarry. At the moment, I tend to like taking at large an OOP approach, and then sprinkling functional concepts within it,
        and haven't really run into a case where it makes sense to start with at large a functional approach and then sprinkle OOP based stuff into that larger persepective, but I'm sure that exists as a good choice for some use case.
    """
#3.Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
    """
    """
#4.Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
    """
        I think to create good code in both paradigms, it would actually probably take equal levels of rigor to understand both, you would just be focusing on different things to write well in each paradigm. 
    """
