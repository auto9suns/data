import numpy as np
import pandas as pd
import string


class randomList():

    @staticmethod
    def generate_random_int(length, low=0, high=100):
        sample_list = np.random.randint(low, high, size = (length,)).tolist()
        return sample_list

    @staticmethod
    def generate_random_float(length, low=0.0, high=100.0):
        sample_list = np.random.uniform(low, high, size =(length,)).tolist()
        return sample_list

    @staticmethod
    def generate_random_pattern(length, pattern_list, pattern_ratio = None):
        sample_list = np.random.choice(a = pattern_list, size = length, replace = True, p = pattern_ratio).tolist()
        return sample_list

    @staticmethod
    def generate_random_letter(length):
        letters = list(string.ascii_letters)
        sample_list = np.random.choice(letters, length, replace= True).tolist()
        return sample_list

    @staticmethod
    def generate_random_string(length, max_digit = 5, extra_mark_list = None):
        letters = list(string.ascii_letters) + extra_mark_list if extra_mark_list else list(string.ascii_letters)
        random_string = lambda x: ''.join(np.random.choice(x, np.random.choice(max_digit)+1).tolist())
        sample_list = [ random_string(letters) for i in range(length)]
        return sample_list



class randomSample():
    def __init__(self, row_number):
        self.data = {}
        self.row_number = row_number

    def add_column(self, colname, data):
        '''
        :param colname: column name string
        :param data: list of data
        :return:
        '''
        if len(data) != self.row_number:
            raise ValueError("self.row_number is {r}, added column length is {l}, add column skipped".format(r=self.row_number, l=len(data)))
        elif colname in self.data.keys():
            raise  ValueError("colname: {r}, add column skipped".format(r=colname))
        else:
            self.data[colname] = data

    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.data)







        



