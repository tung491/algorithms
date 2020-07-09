def is_monotic(input_list):
    no_desc = True
    no_asc = True

    for i in range(1, len(input_list)):
        diff = input_list[i] - input_list[i - 1]
        if diff < 0:
            no_desc = False
        elif diff > 0:
            no_asc = False
    return no_asc or no_desc


def test():
    print(is_monotic([1, 1, 1, 2, 3]))
    print(is_monotic([-2, 3, 1, 3]))



if __name__ == '__main__':
    test()
