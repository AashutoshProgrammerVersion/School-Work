import random


list_of_dad_jokes = []
class DadJokes():
   
   # self.__Prompt string
   # self.__Answer string
   def __init__(self, Prompt, Answer):
       self.__Prompt = Prompt
       self.__Answer = Answer

   def PrintRandomJoke(self):
       random_joke = list_of_dad_jokes[random.randint(0, 9)]

       print(random_joke.__Prompt)
       answer_from_user = input("Write your answer: ")
       print(random_joke.__Answer)


some_object = DadJokes("","")

with open('DadJokes.txt') as file:
   
    for i in range(10):
        prompt = file.readline().strip()
        answer = file.readline().strip()

        list_of_dad_jokes.append(DadJokes(prompt, answer))


some_object.PrintRandomJoke()