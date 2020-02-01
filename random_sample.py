import numpy as np
import pandas as pd
import string, names


class randomList():
    states_initial = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                      "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                      "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                      "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                      "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
              "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
              "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
              "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    @staticmethod
    def generate_random_int(length, low=0, high=100):
        sample_list = np.random.randint(low, high, size=(length,)).tolist()
        return sample_list

    @staticmethod
    def generate_random_float(length, low=0.0, high=100.0):
        sample_list = np.random.uniform(low, high, size=(length,)).tolist()
        return sample_list

    @staticmethod
    def generate_random_pattern(length, pattern_list, pattern_ratio=None):
        sample_list = np.random.choice(a=pattern_list, size=length, replace=True, p=pattern_ratio).tolist()
        return sample_list

    @staticmethod
    def generate_random_letter(length):
        letters = list(string.ascii_letters)
        sample_list = np.random.choice(letters, length, replace=True).tolist()
        return sample_list

    @staticmethod
    def generate_random_string(length, max_digit=5, extra_mark_list=None):
        letters = list(string.ascii_letters) + extra_mark_list if extra_mark_list else list(string.ascii_letters)
        random_string = lambda x: ''.join(np.random.choice(x, np.random.choice(max_digit) + 1).tolist())
        sample_list = [random_string(letters) for i in range(length)]
        return sample_list

    @staticmethod
    def generate_random_english_name(length, type=None, gender=False):
        '''
        :param length: integer
        :param type: 'first' : first name , 'last': last name, other: full name
        :param gender: string male or female
        :return: list of name samples
        '''
        if type and type.lower() == 'first':
            return [names.get_first_name(gender=gender) for i in range(length)]
        elif type and type.lower() == 'last':
            return [names.get_last_name() for i in range(length)]
        else:
            return [names.get_full_name(gender=gender) for i in range(length)]

    @staticmethod
    def generate_random_state(length, abbreviation = False):
        if abbreviation:
            return [randomList.states_initial[i] for i in randomList.generate_random_int(length,0,49)]
        else:
            return [randomList.states[i] for i in randomList.generate_random_int(length,0,49)]


class randomSample():
    def __init__(self, row_number=10):
        self.data = {}
        self.row_number = row_number

    def add_column(self, colname, data):
        '''
        :param colname: column name string
        :param data: list of data
        :return:
        '''
        if len(data) != self.row_number:
            raise ValueError(
                "self.row_number is {r}, added column length is {l}, add column skipped".format(r=self.row_number,
                                                                                                l=len(data)))
        elif colname in self.data.keys():
            raise ValueError("colname: {r}, add column skipped".format(r=colname))
        else:
            self.data[colname] = data

    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.data)

    def update_row_number(self, row_number):
        self.row_number = row_number
