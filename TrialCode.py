import random
import string
import datetime




def atomic_data_types_game():

    player_lives = 5
    player_score = 0
    print(f"Welcome to the Atomic Data Types Game! You have {player_lives} lives and {player_score}. You will be awarded points between 0 to 60 points depending on how many seconds you take (you get 60 seconds but going over it will give you negative points even if you get it correct) \n\n\n")



    def player_lives_checker():
        nonlocal player_lives

        player_lives -= 1

        if player_lives > 0:
            print(f"Incorrect! Try again. You have {player_lives} lives left.")
            points_scored, user_input = points_calculator()
            return points_scored, user_input

        elif player_lives == 0:
            print(f"Game Over! You have {player_lives} lives left and had a total score of {player_score}.")
            restart_or_not = input(f"Would you like to play again? (yes or no) \n")

            while restart_or_not != "yes" and restart_or_not != "no":
                restart_or_not = input(f"Would you like to play again? (yes or no)\n")

            if restart_or_not == "yes":
                print("\n\n\n\n")
                atomic_data_types_game()
            else:
                print("\n\nThank you for playing the Atomic Data Types Game! Bye!")



    def points_calculator():

        start_time = datetime.datetime.now()
        user_input = input(f"What is data type is this (type in all capital without spaces): {random_data_type_object} ? \n")
        end_time = datetime.datetime.now()
        time_taken = end_time - start_time

        return (60 - int(time_taken.seconds)), user_input




    while player_lives > 0:
        
        random_number = random.randint(1, 6)

        if random_number == 1:
            random_data_type_object = random.randint(random.randint(-1000, 0), random.randint(0, 1000))
            points_scored, user_input = points_calculator()

            while user_input != "INTEGER":
                points_scored, user_input = player_lives_checker()

            if user_input == "INTEGER":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")


        if random_number == 2:
            random_data_type_object = round(random.uniform(random.randint(-1000, 0), random.randint(0, 1000)), random.randint(1, 5))
            points_scored, user_input = points_calculator()

            while user_input != "FLOAT":
                points_scored, user_input = player_lives_checker()

            if user_input == "FLOAT":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")


        if random_number == 3:
            characters = string.ascii_letters + string.digits + string.punctuation
            random_data_type_object = ''.join(random.choice(characters) for i in range(random.randint(1, 15)))
            points_scored, user_input = points_calculator()

            while user_input != "STRING":
                points_scored, user_input = player_lives_checker()

            if user_input == "STRING":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")


        if random_number == 4:
            characters = string.ascii_letters + string.digits + string.punctuation
            random_data_type_object = str(random.choice(characters))
            points_scored, user_input = points_calculator()
        
            while user_input != "CHAR":
                points_scored, user_input = player_lives_checker()

            if user_input == "CHAR":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")


        if random_number == 5:
            random_data_type_object = random.choice([True, False])
            points_scored, user_input = points_calculator()
        
            while user_input != "BOOLEAN":
                points_scored, user_input = player_lives_checker()
            
            if user_input == "BOOLEAN":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")


        if random_number == 6:
            random_data_type_object  = datetime.date(random.randint(1, 10000), random.randint(1, 12), random.randint(1, 31))
            points_scored, user_input = points_calculator()

            while user_input != "DATE":
                points_scored, user_input = player_lives_checker()

            if user_input == "DATE":
                player_score += points_scored
                print(f"Correct! You have a total score of {player_score}.\n")




atomic_data_types_game()