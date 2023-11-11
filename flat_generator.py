import types


def flat_generator(list_of_lists):
    counter = 0
    while counter < len(list_of_lists):
        for item in list_of_lists[counter]:
            yield item
        counter += 1

        
        # yield list_of_lists[counter]
        # counter += 1
        
        # for item in list_of_lists[counter]:
        #     yield item
        #     counter += 1


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    