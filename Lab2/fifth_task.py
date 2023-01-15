from fourth_task import my_next


class FileIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self, file_name: str = '../Lab1/dataset.csv'):
        if self.counter < self.limit:
            self.counter += 1
            return my_next(self.counter, file_name)
        else:
            raise StopIteration


if __name__ == '__main__':
    a = FileIterator(10)
    print(next(a))
