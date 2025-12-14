from yahtzee import Yahtzee
import unittest

class TestYahtzee(unittest.TestCase):
    
    def test_chance_scores_sum_of_all_dice(self):
        self.assertEqual(15, Yahtzee.score_chance(2,3,4,5,1), "Score should be 15 as 2+3+4+5+1 = 15")
        self.assertEqual(16, Yahtzee.score_chance(3,3,4,5,1), "Score should be 16 as 3+3+4+5+1 = 16")
  
    def test_yahtzee_scores_50(self):
        self.assertEqual(50, Yahtzee.score_yahtzee(4,4,4,4,4), "Score should be 50 as all values in this roll are equal (4s)")
        self.assertEqual(50, Yahtzee.score_yahtzee(6,6,6,6,6), "Score should be 50 as all values in this roll are equal (6s)")
        self.assertEqual(0, Yahtzee.score_yahtzee(6,6,6,6,3), "Score should be 0 as all values in this roll aren't equal")


    def Test_1s(self):
        self.assertEqual(0, Yahtzee.score_ones(1,2,1,4,5), "Score should be 0 as there is 0x '1' in this roll")
        self.assertEqual(1, Yahtzee.score_ones(1,2,3,4,5), "Score should be 1 as there is 1x '1' in this roll")
        self.assertEqual(2, Yahtzee.score_ones(1,2,1,4,5), "Score should be 2 as there is 2x '1' in this roll")
        self.assertEqual(4, Yahtzee.score_ones(1,2,1,4,5), "Score should be 4 as there is 4x '1' in this roll")
    
    def test_2s(self):
        self.assertEqual(0, Yahtzee.score_twos(1,6,3,6,6), "Score should be 0 as there is 0x '2' in this roll")
        self.assertEqual(4, Yahtzee.score_twos(1,2,3,2,6), "Score should be 4 as there is 2x '2' in this roll")
        self.assertEqual(10, Yahtzee.score_twos(2,2,2,2,2), "Score should be 10 as there is 5x '2' in this roll")


    def test_threes(self):
        self.assertEqual(0, Yahtzee.score_threes(2,4,2,1,1), "Score should be 0 as there is 0x '3' in this roll")
        self.assertEqual(6, Yahtzee.score_threes(1,2,3,2,3), "Score should be 6 as there is 2x '3' in this roll")
        self.assertEqual(12, Yahtzee.score_threes(2,3,3,3,3), "Score should be 12 as there is 4x '3' in this roll")
  
    def test_fours_test(self):
        self.assertEqual(0, Yahtzee.score_fours(5,5,5,5,5), "Score should be 0 as there is 0x '4' in this roll")
        self.assertEqual(12, Yahtzee.score_fours(4,4,4,5,5), "Score should be 12 as there is 3x '4' in this roll")
        self.assertEqual(8, Yahtzee.score_fours(4,4,5,5,5), "Score should be 8 as there is 2x '4' in this roll")
        self.assertEqual(4, Yahtzee.score_fours(4,5,5,5,5), "Score should be 12 as there is 1x '4' in this roll")

    def test_fives(self):
        self.assertEqual(0, Yahtzee.score_fives(4,4,4,4,4), "Score should be 0 as there is 0x '5' in this roll")
        self.assertEqual(10, Yahtzee.score_fives(4,4,4,5,5), "Score should be 10 as there is 2x '5' in this roll")
        self.assertEqual(15, Yahtzee.score_fives(4,4,5,5,5), "Score should be 15 as there is 3x '5' in this roll")
        self.assertEqual(20, Yahtzee.score_fives(4,5,5,5,5), "Score should be 8 as there is 2x '5' in this roll")

    def test_sixes_test(self):
        self.assertEqual(0, Yahtzee.score_sixes(4,4,4,5,5), "Score should be 0 as there is 0x '6' in this roll")
        self.assertEqual(6, Yahtzee.score_sixes(4,4,6,5,5), "Score should be 10 as there is 1x '6' in this roll")
        self.assertEqual(18, Yahtzee.score_sixes(6,5,6,6,5), "Score should be 8 as there is 3x '6' in this roll")


    def test_one_pair(self):
        self.assertEqual(0, Yahtzee.score_pair(3,3,3,3,5), "Score should be 0 as there is no valid pair")
        self.assertEqual(6, Yahtzee.score_pair(3,4,3,5,6), "Score should be 6 as there is exactly 2x 3 in this roll (3+3 = 6)")
        self.assertEqual(12, Yahtzee.score_pair(3,6,3,5,6), "Score should be 12 as there is exactly 2x 3 in this roll and 2x 6 but 6 > 3")
        self.assertEqual(10, Yahtzee.score_pair(5,3,3,3,5), "Score should be 10 as there is exactly 2x 5 in this roll (5+5 = 10)")



  

    def test_two_Pair(self):
        self.assertEqual(16, Yahtzee.score_two_pair(3,3,5,4,5), "Score should be 16 as there is exactly 2x 3 and 2x 5 in this roll (2 + 2 + 5 + 5 = 16)")
        self.assertEqual(0, Yahtzee.score_two_pair(3,3,5,5,5), "Score should be 0 as there is exactly 2x 3 but not exactly 2x 5 in this roll")


    def test_three_of_a_kind(self):
        self.assertEqual(9, Yahtzee.score_three_of_a_kind(3,3,3,4,5), "Score should be 16 as there is exactly 3x 3 in this roll (3 + 3 + 3 = 9)")
        self.assertEqual(0, Yahtzee.score_three_of_a_kind(3,3,3,3,5), "Score should be 0 as there is not exactly 3x 3 this roll")
        self.assertEqual(15, Yahtzee.score_three_of_a_kind(5,3,5,4,5), "Score should be 0 as there is not exactly 3x 3 this roll")


    def test_four_of_a_knd(self):
        self.assertEqual(12, Yahtzee.score_four_of_a_kind(3,3,3,3,5), "Score should be 12 as there is not exactly 4x 3 this roll (3+3+3+3 = 12)")
        self.assertEqual(20, Yahtzee.score_four_of_a_kind(5,5,5,4,5), "Score should be 20 as there is not exactly 4x 5 this roll (5+5+5+5 = 12)")
        self.assertEqual(0, Yahtzee.score_four_of_a_kind(3,3,3,3,3), "Score should be 0 as there is not exactly 4x 3 this roll")
  

    def test_smallStraight(self):
        self.assertEqual(15, Yahtzee.score_small_straight(1,2,3,4,5), "Score should be 15 as there is a small straight present")
        self.assertEqual(15, Yahtzee.score_small_straight(2,3,4,5,1), "Score should be 15 as there is a small straight present")
        self.assertEqual(0, Yahtzee.score_small_straight(1,2,2,4,5), "Score should be 0 as there is NOT a small straight present")

  
    def test_largeStraight(self):
        self.assertEqual(20, Yahtzee.score_large_straight(6,2,3,4,5), "Score should be 20 as there is a large straight present")
        self.assertEqual(20, Yahtzee.score_large_straight(2,3,4,5,6), "Score should be 20 as there is a large straight present")
        self.assertEqual(0, Yahtzee.score_large_straight(1,2,2,4,5), "Score should be 0 as there is NOT a large straight present")

  


    def test_fullHouse(self):
        self.assertEqual(18, Yahtzee.score_full_house(6,2,2,2,6), "Score should be 18 as there is exactly 3x '2' and 2x '6' (2+2+2+6+6 = 16)")
        self.assertEqual(22, Yahtzee.score_full_house(6,6,2,2,6), "Score should be 18 as there is exactly 3x '6' and 2x '2' (2+2+6+6+6 = 22)")
        self.assertEqual(0, Yahtzee.score_full_house(2,3,4,5,6), "Score should be 18 as there is exactly 3x One number and 2x Another Number")


   

if __name__ == '__main__':
    unittest.main()