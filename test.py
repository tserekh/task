import random
import pandas as pd
from report import report
import unittest


def test_data():
    dics = []
    for i in range(1, 100):
        for _ in range(i):
            dic = {}
            dic['OrderID'] = random.randint(1, 100)
            dic['CustomerID'] = random.randint(1, 100)
            dic['DateTime'] = pd.Timestamp(2019, 7, 23, 1, 1, 1)
            dic['ProductID'] = i
            dic['price'] = 1
            dics.append(dic)

    df_data = pd.DataFrame(dics)
    df_orders = df_data[['DateTime', 'OrderID']].drop_duplicates()
    df_lines = df_data[['ProductID', 'OrderID', 'price']]
    return df_orders, df_lines


result = report(*test_data())


class TestUM(unittest.TestCase):

    def test_producsts(self):
        result = report(*test_data())
        self.assertEqual(set(result.index), set(
            [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]))

    def test_revenue(self):
        self.assertEqual((result['total_revenue'] == result.index).mean(), 1)


if __name__ == '__main__':
    unittest.main()
