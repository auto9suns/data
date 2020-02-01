from random_sample import randomList, randomSample
import unittest
import numpy as np


class test_randomList(unittest.TestCase):

    def setUp(self):
        np.random.seed(10)

    def test_generate_random_int(self):
        case1 = randomList.generate_random_int(10,0,5)
        case2 = randomList.generate_random_int(10)
        self.assertEqual(len(case1),10)
        self.assertEqual(len(case2),10)
        for i in case1:
            self.assertGreaterEqual(i, 0)
            self.assertLess(i,5)

    def test_generate_random_float(self):
        case1 = randomList.generate_random_float(10, 0.0, 1)
        case2 = randomList.generate_random_float(10)
        self.assertEqual(len(case1),10)
        self.assertEqual(len(case2),10)
        self.assertEqual(case1, [0.771320643266746, 0.0207519493594015, 0.6336482349262754, 0.7488038825386119,
                                 0.4985070123025904, 0.22479664553084766, 0.19806286475962398, 0.7605307121989587,
                                 0.16911083656253545, 0.08833981417401027])
        self.assertEqual(case2,[68.53598183677973, 95.33933461949366, 0.39482663279144514, 51.21922633857766,
                                81.26209616521135, 61.25260668293882, 72.17553174317996, 29.187606817063315,
                                91.77741225129435, 71.45757833976906])



    def test_generate_random_pattern(self):
        case1 = randomList.generate_random_pattern(10,['a','b','c'])
        case2 = randomList.generate_random_pattern(100,['a','b','c'],pattern_ratio=[0.1,0.3,0.6])
        case3 = randomList.generate_random_pattern(100,['a','b','c'],pattern_ratio=[0.2,0.8, 0 ])
        self.assertEqual(len(case1),10)
        self.assertEqual(len(case2),100)
        self.assertEqual(len(case3),100)
        self.assertEqual(case1, ['b', 'b', 'a', 'a', 'b', 'a', 'b', 'b', 'a', 'b'])
        self.assertEqual(case2, ['b', 'c', 'b', 'a', 'c', 'c', 'a', 'c', 'c', 'c', 'c', 'b', 'c', 'c', 'c', 'b', 'b',
                                 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', 'a', 'b', 'b', 'c', 'a', 'c',
                                 'c', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'b', 'b', 'a', 'c', 'b', 'b', 'c', 'c',
                                 'c', 'c', 'b', 'c', 'c', 'c', 'c', 'a', 'b', 'a', 'b', 'b', 'c', 'a', 'c', 'b', 'c',
                                 'b', 'a', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'b', 'b', 'a', 'b', 'b', 'c', 'c', 'c',
                                 'b', 'a', 'c', 'b', 'c', 'c', 'c', 'b', 'c', 'c', 'c', 'a', 'c', 'c', 'c'])
        self.assertEqual(case3,['b', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'b', 'a', 'a', 'b', 'b', 'b', 'b', 'a',
                                'b', 'b', 'b', 'a', 'a', 'b', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b',
                                'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'a', 'b', 'a', 'b', 'b', 'a', 'b', 'b',
                                'b', 'a', 'b', 'b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'b', 'b', 'b',
                                'b', 'a', 'b', 'a', 'b', 'b', 'b', 'b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b', 'a',
                                'b', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'b', 'b', 'b'])


    def test_generate_random_letter(self):
        case1 = randomList.generate_random_letter(10)
        self.assertEqual(len(case1),10)
        self.assertEqual(case1, ['j', 'K', 'p', 'a', 'X', 'C', 'z', 'D', 'W', 'D'])


    def test_generate_random_sting(self):
        case1 = randomList.generate_random_string(10)
        self.assertEqual(len(case1),10)
        self.assertEqual(case1,['Kp', 'X', 'CzDW', 'ij', 'Q', 'K', 'qKVl', 'R', 'HiK', 'Zn'])


    def test_generate_random_english_name(self):
        randomList.generate_random_english_name(10)
        randomList.generate_random_english_name(10, type='first')
        randomList.generate_random_english_name(10, type='last')
        randomList.generate_random_english_name(10, type='first', gender='male')

    def test_generate_random_state(self):
        a = randomList.generate_random_state(5)
        b = randomList.generate_random_state(5,True)
        self.assertEqual(a, ['Georgia', 'Oregon', 'Kansas', 'Alabama', 'New Hampshire'])
        self.assertEqual(b,  ['MO', 'NH', 'WV', 'NH', 'DE'])






class test_randomSample(unittest.TestCase):

    def setUp(self):
        np.random.seed(10)
        self.rs = randomSample(5)

    def test_add_column(self):
        self.rs.add_column("col1",[1,2,3,4,5])
        self.rs.add_column("col2",['a','b','c','d','e'])
        self.assertEqual(self.rs.data, {"col1":[1,2,3,4,5], "col2":['a','b','c','d','e']})
        self.assertRaises(ValueError,self.rs.add_column, "col",["1"])
        self.assertRaises(ValueError, self.rs.add_column, "col1", ['a','b','c','d','e'])

    def test_get_dataframe(self):
        self.rs.add_column("col1",[1,2,3,4,5])
        self.rs.add_column("col2",['a','b','c','d','e'])
        df = self.rs.get_dataframe()
        self.assertEqual(df.columns.tolist(), ['col1','col2'])

    def test_update_row_number(self):
        self.rs.update_row_number(20)
        self.assertEqual(self.rs.row_number, 20)
















