class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1
        self.len_list_of_lists = len(list_of_list)

    def __iter__(self):
        self.counter += 1
        return self

    def __next__(self):
        if self.counter <= self.len_list_of_lists:
            list_1 = self.list_of_list[self.counter]
            for item in list_1:
                # print(item)
                return item
        else:
            raise StopIteration
        return self.counter


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()