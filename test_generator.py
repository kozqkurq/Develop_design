def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data

def main():
    for data in (x for x in range(1, 6)):
        print(data)
        if data > 2:
            break

main()