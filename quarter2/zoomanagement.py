#parent class
class Animal:
    def __init__(self, name): #special constructor method
        self.name = name

    #original methods
    def eat(self):
        print(self.name,"is eating.")

    def sleep(self):
        print(self.name,"is sleeping.")

    @property
    def make_sound(self):
        print(self.name,"makes a sound.")

#child class 1
class Lion(Animal):

    #overridden methods:
    @property
    def make_sound(self):
        print(self.name,"roars loudly!")
    
    @property
    def eat(self):
        print(self.name,"eats fresh meat.")

    #the make_sound and eat methods are altered, compared to the original method in the parent class

#child class 2
class Elephant(Animal):

    #overridden methods:
    @property
    def make_sound(self):
        print(self.name,"trumpets!")

    @property
    def eat(self):
        print(self.name,"eats grass and fruits.")

    #same as the previous child class, the two methods are also altered

#child class 3
class Monkey(Animal):

    #overridden methods:
    @property
    def make_sound(self):
        print(self.name,"chatters!")

    @property
    def eat(self):
        print(self.name,"eats bananas.")

    #same as the previous classes

#object creation
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound
lion.eat
print("-----")
elephant.make_sound
elephant.eat
print("-----")
monkey.make_sound
monkey.eat
print("-----")

#each time the methods are called there are different outputs because the method was overridden
#note: Good evening, sir. I used the @property decorator to apply what I have learned last meeting.
#so, instead of using lion.make_sound(), i used lion.make_sound