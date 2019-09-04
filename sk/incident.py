import pandas as pd
import numpy as np
import time
import argparse
from collections import defaultdict


def incident(dT, filename, output='output.csv'):

    file = open(filename)
    headers = file.readline()
    num_features = len(headers.split(','))-2
    dic = defaultdict(list)

    for line in file:
        line_splitted = line[:-1].split(',')
        dic[tuple(line_splitted[1:-1])
            ].append((int(line_splitted[0]), float(line_splitted[-1])))
    file.close()

    response = [0]*(1+int(line_splitted[0]))

    def add_responses(arr, response):
        times = []
        for id_, mytime in arr:
            counter = 0

            for time in times:
                if mytime-time < dT:

                    counter += 1
            response[id_] = counter

            times.append(mytime)

    for key in dic.keys():
        dic[key].sort(key=lambda x: x[1])
        add_responses(dic[key], response)

    with open(output, mode='w') as file:
        file.write('id,count\n')
        for id_, count in enumerate(response):
            file.write(str(id_)+','+str(count)+'\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    parser.add_argument('--dt')
    args = parser.parse_args()
    incident(float(args.dt), args.input, output=args.output)
