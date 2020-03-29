import numpy as np
import pandas as pd
import string, json
from faker import Faker
from faker.providers import person, address, color, date_time, company


class cumstomData():
    state = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC',
             'Deleware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinios', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
             'Louisiana',
             'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
             'Nebraska',
             'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
             'Ohio', 'Oklahoma',
             'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
             'Vermont', 'Virgina', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    state_abbr = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                  'KY',
                  'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
                  'OH',
                  'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    popular_city_state = {'New York': 'New York', 'Los Angeles': 'California', 'Chicago': 'Illinois', 'Houston': 'Texas', 'Phoenix': 'Arizona', 'Philadelphia': 'Pennsylvan', 'San Antonio': 'Texas', 'San Diego': 'California', 'Dallas': 'Texas', 'San Jose': 'California', 'Austin': 'Texas', 'Jacksonville': 'Florida', 'Fort Worth': 'Texas', 'Columbus': 'Ohio', 'San Francisco': 'California', 'Charlotte': 'North Caro', 'Indianapolis': 'Indiana', 'Seattle': 'Washington', 'Denver': 'Colorado', 'Washington': 'District o', 'Boston': 'Massachuse', 'El Paso': 'Texas', 'Detroit': 'Michigan', 'Nashville': 'Tennessee', 'Portland': 'Oregon', 'Memphis': 'Tennessee', 'Oklahoma City': 'Oklahoma', 'Las Vegas': 'Nevada', 'Louisville': 'Kentucky', 'Baltimore': 'Maryland', 'Milwaukee': 'Wisconsin', 'Albuquerque': 'New Mexico', 'Tucson': 'Arizona', 'Fresno': 'California', 'Mesa': 'Arizona', 'Sacramento': 'California', 'Atlanta': 'Georgia', 'Kansas City': 'Missouri', 'Colorado Springs': 'Colorado', 'Miami': 'Florida', 'Raleigh': 'North Caro', 'Omaha': 'Nebraska', 'Long Beach': 'California', 'Virginia Beach': 'Virginia', 'Oakland': 'California', 'Minneapolis': 'Minnesota', 'Tulsa': 'Oklahoma', 'Arlington': 'Texas', 'Tampa': 'Florida', 'New Orleans': 'Louisiana'}


class randomData():
    providers = [person, address, color, date_time, company]

    def __init__(self):
        self.fakers = {}
        self.current_faker = self.new_faker()


    def add_providers(self, faker):
        for provider in randomData.providers:
            faker.add_provider(provider)

    def new_faker(self, locale=None):
        '''
        local string check https://faker.readthedocs.io/en/stable/index.html
        zh_CN: Chinese
        en_US: US
        '''
        new_faker = Faker(locale)
        self.add_providers(new_faker)
        if locale:
            self.fakers[locale] = new_faker
        else:
            self.fakers["en_US"] = new_faker
        return new_faker

    def set_current_faker(self, locale=None):
        if locale:
            if locale not in self.fakers.keys():
                self.new_faker(locale)
            self.current_faker = self.fakers[locale]
        else:
            self.current_faker = self.fakers["en_US"]

    def random_int(self, low=0, high=100):
        return np.random.randint(low, high)

    def random_float(self, low=0.0, high=100.0):
        return np.random.uniform(low, high)

    def random_pattern(self, pattern_list, pattern_ratio=None):
        return np.random.choice(a=pattern_list, replace=True, p=pattern_ratio)

    def random_letter(self):
        letters = list(string.ascii_letters)
        return np.random.choice(letters, replace=True)

    def random_string(self, max_digit=5, extra_mark_list=None):
        letters = list(string.ascii_letters) + extra_mark_list if extra_mark_list else list(string.ascii_letters)
        random_string = lambda x: ''.join(np.random.choice(x, np.random.choice(max_digit) + 1).tolist())
        sample_list = [random_string(letters) for i in range(1)]
        return sample_list

    def random_firstname(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.first_name()

    def random_lastname(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.last_name()

    def random_name(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.name()

    def random_date(self, pattern='%Y-%m-%d', end_datetime=None, locale=None):
        '''
        :param pattern:
        :param end_datetime: cant be 'today' as today
        :return:
        '''
        self.set_current_faker(locale)
        return self.current_faker.date(pattern='%Y-%m-%d', end_datetime=None, locale=None)

    def random_date_this_year(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.date_this_year()

    def random_date_time_this_month(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.date_time_this_month()

    def random_state_abbr(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.state_abbr()

    def random_state(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.state()

    def random_city(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.city()

    def random_company(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.company()

    def random_address(self, locale=None):
        self.set_current_faker(locale)
        return self.current_faker.address()

    def random_popular_city(self):
        return self.random_pattern(list(cumstomData.popular_city_state.keys()))



class randomSample():
    def __init__(self, name = "mysample",row_number=10):
        self.data = {}
        self.name = name
        self.row_number = row_number
        self.rd = randomData()

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

    def generate_func_data(self, func, length, args=None):
        '''
        :param func: function name in Random Data without random prefix,
        :param args: args are arguments dict
        :return:
        '''
        func = getattr(self.rd, "random_" + func)
        if args:
            return [func(**args) for i in range(length)]
        else:
            return [func() for i in range(length)]

    def generate_align_data(self, func,  align_col, args = None):
        align_col_unique_data = set(self.data[align_col])
        cnt_unique = len(align_col_unique_data)
        target_col_unique = self.generate_func_data(func, cnt_unique, args)
        zipped_data = {k: v for k, v in zip(align_col_unique_data, target_col_unique)}
        return [zipped_data[i] for i in self.data[align_col]]


    def generate_col(self, func = None, args=None, align_col=None, mapping = None, root_col = None):
        '''
        :param func: name of func with out random prefix
        :param args: arguments dict for func
        :param align_col: if column B's align_col is A then A and B are 1:1 mapping
        :param mapping: if column B's mapping is mapping = {} and root_col is A, then b = mapping[A]
        只有三种情况
        1. func_name with or without args
        2. func_name with or without args, align_col
        3. mapping, root_col
        :return:
        '''

        if mapping and root_col:
            return [getattr(cumstomData, mapping)[i] for i in self.data[root_col]]
        elif not align_col and func:
            return self.generate_func_data(func, self.row_number, args)
        elif align_col and func:
            return self.generate_align_data(func, align_col, args)
        else:
            print ("argument error")


    def get_dataframe(self):
        df = pd.DataFrame.from_dict(self.data)
        return df[list(self.data.keys())]

    def update_row_number(self, row_number):
        self.row_number = row_number

    def deduplicate(self, df):
        df.drop_duplicates(inplace= True)
        return df


def main(config_path):
    config = parse_config(config_path)
    for table in config:
        rs = randomSample(table.get("name"), table.get("size"))
        for column in table.get("columns"):
            data = rs.generate_col(column.get("func"), column.get("args"), column.get("align_col"), column.get("mapping"), column.get("root_col"))
            rs.add_column(column.get("name"), data)
        df = rs.get_dataframe()
        print(df.columns)
        print(df.head(10))
        df.drop_duplicates(inplace=True)
        df.to_csv(rs.name + ".csv", index=False)


def parse_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def python_object_from_file(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            data.append(line)
    print (data)


if __name__ == "__main__":
    pd.set_option('expand_frame_repr', False)
    main("sample.json")
