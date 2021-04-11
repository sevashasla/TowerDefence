import pocket

# uses MoneyError, which is to be implemented


def unit_tests_for_Pocket():
    a = pocket.Pocket()
    dengi = a.getMoney()
    print(dengi)
    dengi = 3
    a.addMoney(dengi)
    print(a.getMoney(), dengi)
    dengi += a.lendMoney(dengi - 1)
    print(a.getMoney(), dengi)
    try:
        dengi += a.lendMoney(5)
    except pocket.MoneyError:
        print('Sorry, we don\'t have enough money ;(')


unit_tests_for_Pocket()
