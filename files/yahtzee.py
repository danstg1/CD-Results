class Yahtzee():
    def __init__(self, d1, d2, d3, d4, d5):
        """
        Initalise Function, never actually used it as creating the object takes up memory and computational complexity for no need
        """
        self.dice = [d1,d2,d3,d4,d5]
    
    
    @staticmethod 
    def setUpCounts(d1,d2,d3,d4,d5):
        """
        Dices [Int] - All the dice faces given
        A method to prevent repeated code. Sets up needed "Counts List"
        """
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        return counts
    
    
    
    @staticmethod
    def score_chance(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        This function adds all the dice values together and returns this value regardless of what is on the roll
        """
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def score_yahtzee(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        This function checks if all dice faces are the same and if they are returns a score of 50
        If they are not then they score 0
        """
        if d1 == d2 == d3 == d4 == d5:
            return 50
        else:
            return 0
    
    @staticmethod
    def getSinglesScore(chosenNumber, dices):
        """
        Single (Int) - The dice face that is to be checked
        Dices [Int] - All the dice faces given
        This function is used for the "Upper Section" of Yahtzee hands
        The player scores the sum of the dice that reads their chosen number of one, two, three, four, five or six
        """
        sum = 0
        for dice in dices:
            if dice == chosenNumber:
                sum += chosenNumber
        return sum
    

    @staticmethod
    def score_ones(d1, d2, d3, d4, d5):
        return Yahtzee.getSinglesScore(1, [d1,d2,d3,d4,d5])
    

    @staticmethod
    def score_twos(d1, d2, d3,  d4,  d5):
        return Yahtzee.getSinglesScore(2, [d1,d2,d3,d4,d5])
    
    @staticmethod
    def score_threes(d1,  d2,  d3,  d4,  d5):
        return Yahtzee.getSinglesScore(3, [d1,d2,d3,d4,d5])


    @staticmethod
    def score_fours(d1,  d2,  d3,  d4,  d5):
        return Yahtzee.getSinglesScore(4, [d1,d2,d3,d4,d5])
    
    
    @staticmethod
    def score_fives(d1,  d2,  d3,  d4,  d5):
        return Yahtzee.getSinglesScore(5, [d1,d2,d3,d4,d5])
    
    
    @staticmethod
    def score_sixes(d1,  d2,  d3,  d4,  d5):
        return Yahtzee.getSinglesScore(6, [d1,d2,d3,d4,d5])
    
    
    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        The scores the sum of the two highest matching dice.
        """
        counts = Yahtzee.setUpCounts(d1, d2, d3, d4, d5)
        pairAt = 0
        for pairAt in range(len(counts)):
            if (counts[5-pairAt] == 2):
                return (6-pairAt)*2
        return 0
    
    
    @staticmethod
    def score_two_pair(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        If there are two pairs of dice with the same number, the player scores the sum of these dice.
        """
        counts = Yahtzee.setUpCounts(d1, d2, d3, d4, d5)
        pairCount = 0
        score = 0
        for i in range(len(counts)):
            if (counts[5-i] == 2):
                pairCount +=1
                score += (6-i)
                    
        if (pairCount == 2):
            return score * 2
        else:
            return 0
        
        
    @staticmethod
    def score_three_of_a_kind(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        If there are three dice with the same number, the player scores the sum of these dice.
        """
        counts = Yahtzee.setUpCounts(d1, d2, d3, d4, d5)
        for i in range(len(counts)):
            if (counts[i] == 3):
                return (i+1) * 3
        return 0

    
    @staticmethod
    def score_four_of_a_kind(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        If there are 4 dice with the same number, the player scores the sum of these dice.
        """
        counts = Yahtzee.setUpCounts(d1, d2, d3, d4, d5)
        for i in range(len(counts)):
            if (counts[i] == 4):
                return (i+1) * 4
        return 0
 
   
    @staticmethod
    def score_small_straight(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        If there is a small straight present (1,2,3,4,5) then returns the score of 15, if there is anything else returns 0
        """
        if sorted([d1,d2,d3,d4,d5]) == [1,2,3,4,5]:
            return 15
        else:
            return 0
    

    @staticmethod
    def score_large_straight(d1, d2, d3, d4, d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        If there is a large straight present (2,3,4,5,6) then returns the score of 20, if there is anything else returns 0
        """
        if sorted([d1,d2,d3,d4,d5]) == [2,3,4,5,6]:
            return 20
        
        else:
            return 0
    

    @staticmethod
    def score_full_house(d1, d2, d3, d4,  d5):
        """
        d1,d2,d3,d4,d4,d5 (Int) - Int representations of a dice face
        Calculates for a Full House
        
        
        NOTE: This can be changed in to calling the "pair" and "3 of a kind" functions but this makes it more complex
        """
        hasTwo = False
        hasTwoat = 0
        hasThree = False
        hasThreeAt = 0
        counts = Yahtzee.setUpCounts(d1, d2, d3, d4, d5)

        for i in range(len(counts)):
            if (counts[i] == 2): 
                hasTwo = True
                hasTwoAt = i+1
            

        for i in range(len(counts)):
            if (counts[i] == 3): 
                hasThree = True
                hasThreeAt = i+1
            

        if (hasTwo and hasThree):
            return hasTwoAt * 2 + hasThreeAt * 3
        else:
            return 0