# constructor and destructor

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f'name: {name} , age: {age}')
    
#     def __del__(self):
#         print(f'Person object for {self.name} is being destroyed.')
    
#     def chek(self):
#         print(f'name: {self.name}') 
            

# # create object
# p = Person('Fuad', 12)
# p.chek()

# # manually delete the object (optional)
# # del p

# # after this line, __del__() will be called automatically





# magic method

# class Book: 
#     def __init__(self , name , author , page):
#         self.name = name
#         self.author = author
#         self.page = page
        
#     #friendly express
#     def __str__(self):
#         return f'"{self.name}" by {self.author}, {self.page} pages.'
    
#     def __repr__(self):
#         return f'Book(title="{self.name}", author="{self.author}", pages={self.page})'
        



# b = Book('chem' , 'fuad' , 12)

# print(b)






# inheritance 


# class Base: 
#     def calculate_area(self, len , wed):
#         self.len = len
#         self.wed = wed
        
#         return self.len * self.wed


# class Rectangle(Base):
#     def calculate_rectangle():






# polymerization

class Dog: 
    def make_sound(self):
        print('woof')
class Cat:
    def make_sound(self):
        print('meew')
class Duck:
    def make_sound(self):
        print('gruu')

def let_them_speak(animal):
    animal.make_sound()
    
c = Cat()
d = Dog()
s = Duck()

let_them_speak(c)
let_them_speak(d)
let_them_speak(s)
    
        
           
        

