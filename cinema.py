films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    film_choice = input("Type the name of the film you want to see: ").strip().title()
    if film_choice in films:
        age = int(input("How old are you? ").strip())

        if age >= films[film_choice][0]:

            if films[film_choice][1] > 0:                
                print("Enjoy the film!")
                films[film_choice][1] = films[film_choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("Sorry, you are not old enough to see {}.".format(film_choice))
    else:
        print("Sorry, we do not have {} showing.".format(film_choice))
            
