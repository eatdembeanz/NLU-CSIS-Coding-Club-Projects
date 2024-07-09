import random
def attacktest(skill, rating):
    roll = random.randint(1,101)
    modroll = roll + rating
    if modroll <= skill:
        print(f"Test was {skill}. Rolled {roll} with a modifier of {rating}. Success!")
    else:
        print(f"Test was {skill}. Rolled {roll} with a modifier of {rating}. Failure!")

attacktest(50,10)