from random import choice

questions = ["Where does the moon go during the day? ", "Why are you so old? ", "What happens if your belly button falls off? "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("But why? ").strip().lower()
    
    
