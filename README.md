
# The-art-of-math
This is a computer game to be written in Pygame, aiming to practice math multiplication.
It is based on the idea of a popular computer game, space invader. After practising, we hope kids will improve the math skills in a more fun and entertain way. 


Inspired by Star War, the space invader will become a rescure mission by M Falcon. The player will be a Jedi who needs to hit the correct target missile, represented by the correct multiplication. 
master


# get random number 1 and number 2
        random_nbr1 = random.randint(1,9)
        random_nbr2 = random.randint(1,9)
        #Nbr1 = pygame.image.load(numberList[random_nbr1])
        #Nbr2 = pygame.image.load(numberList[random_nbr2])
        #print("falcon" + str(random_nbr1) + str(random_nbr2) + ".jpg")
        falcon = pygame.image.load("falcon" + str(random_nbr1) + str(random_nbr2) + ".png")
