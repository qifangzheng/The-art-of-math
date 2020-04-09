 # load n -1 other random answers
        randomIndex = []       # the index of the four random results
        resultImg = []         # array to load the four results and the correct result
        for i in range(0,n-1):
            randomAnswer = random.randint(0,35)
        
            # skip the correct result and repeated random results
            while randomAnswer == resultIndex or randomAnswer in randomIndex:
                randomAnswer = random.randint(0,35)
    
            randomIndex.append(randomAnswer)
            resultImg.append(pygame.image.load(resultList[randomAnswer]))

        #add the correct answer to a random position in the array
        answerPosition = random.randint(0,n-1)
        resultImg.insert(answerPosition, pygame.image.load(str(result) + ".png"))
        