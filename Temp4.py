class TEST:
    def __init__(self):
        print("기메ㅐ륑")

def test(class_name):
    print(type(class_name))
    print(TEST)
    if type(class_name) == TEST:
        print("된다.")
    else:
        print("안된다.")


if __name__ == "__main__":
    t = TEST()

    test(t)