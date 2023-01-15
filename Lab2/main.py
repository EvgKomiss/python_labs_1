import pandas
from first_task import first_task
from second_task import second_task
from third_task import third_task



if __name__ == '__main__':
    dataframe = pandas.read_csv("../Lab1/dataset.csv")
    first_task(dataframe)
    second_task(dataframe)
    third_task(dataframe)
