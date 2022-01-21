from collections import MutableMapping


def flatten(dictionary, parent_key=False, separator='.'):
    """
    Turn a nested dictionary into a flattened dictionary
    :param dictionary: The dictionary to flatten
    :param parent_key: The string to prepend to dictionary's keys
    :param separator: The string used to separate flattened keys
    :return: A flattened dictionary
    """

    items = []
    for key, value in dictionary.items():

        new_key = str(parent_key) + separator + key if parent_key else key
        if isinstance(value, MutableMapping):

            if not value.items():
                items.append((new_key, None))
            else:
                items.extend(flatten(value, new_key, separator).items())
        elif isinstance(value, list):
            if len(value):
                for k, v in enumerate(value):
                    items.extend(flatten({str(k): v}, new_key).items())
            else:
                items.append((new_key, None))
        else:
            items.append((new_key, value))
    return dict(items)


if __name__ == '__main__':

    ans = flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y': 10}},
                   'd': [1, 2, 3], 'e': {'f': [], 'g': {}}})
    print('\nflattened:', ans)
