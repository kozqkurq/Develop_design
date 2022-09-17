def test_closure(check_value):
    data = []

    def add_data(checked_value):
        if checked_value < check_value:
            data.append(checked_value)

    def get_data():
        return data

    return add_data, get_data


if __name__ == "__main__":
    add_data, get_data = test_closure(5)

    for i in range(10):
        add_data(i)

    data = get_data()
    print(data)