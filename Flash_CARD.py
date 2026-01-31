import random

class Flashcard:
    
    def __init__(self):
        
        self.__fruits = {
            
            'banana':'yellow',
            'apple' :'green',
            'strawberry':' pinik'
        }
        
    def quiz(self):
        
        while True:

            fruit,color = random.choices(list(self.__fruits.items()))[0]

            print('What is the color of {}'.format(fruit))
            user_answer = input()

            if user_answer.lower() == color:
                print('Sahi jawab')
            else:
                print('Galat jawab')

            option = int(input('enter 0 to play again 1 to exit'))

            if option:
                break
              
print('Welcome to the quiz game')
fc = Flashcard()

fc.quiz()            