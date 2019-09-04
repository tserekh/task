import pandas as pd
import numpy as np
from collections import defaultdict
import time
import unittest
from incident import incident


def brute_force(dT, filename):

    df = pd.read_csv(filename, dtype={'id': np.int32})
    conter_list = []
    id_list = []
    for i, row1 in df.iterrows():
        counter = 0
        for j, row2 in df.iterrows():
            if min(row1.iloc[1:-1] == row2.iloc[1:-1]) and (row1['id'] != row2['id']):
                if 0 < (row1['time'] - row2['time']) <= dT:
                    counter += 1
        conter_list.append(counter)
    return conter_list


class TestStringMethods(unittest.TestCase):
    def calc_test(self, dT, filename):

        incident(dT, filename)
        conter_list = brute_force(dT, filename)
        df_output = pd.read_csv('output.csv')
        df_output['check'] = conter_list
        self.assertTrue((df_output['count'] == df_output['check']).min())

    def test1(self):
        self.calc_test(dT=0.3, filename='test1.csv')

    def test2(self):
        self.calc_test(dT=0.5, filename='test2.csv')


if __name__ == '__main__':
    unittest.main()
