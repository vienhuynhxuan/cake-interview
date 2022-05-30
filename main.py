from load_data import load_data


def is_missing(a, b):
    delta = abs(a - b)
    if delta == 1 or delta == 5 or delta > 100:
        return False
    return True


if __name__ == '__main__':
    entries = load_data()
    point = next(entries)
    for i, value in enumerate(entries):
        if is_missing(point, value):
            print(f"A number is missing at indexes ({i}, {i + 1}) and values ({point}, {value}) => Missing value: {max(point, value) + 101}")
        point = value