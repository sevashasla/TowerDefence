import Game


class MoneyError(Exception):
    pass


class Pocket:

        __isinstance = None

        money = 0

        def __init__(self):
            if not Pocket.__isinstance:
                pass
            else:
                self.getInstance()

        @classmethod
        def getInstance(cls):
            if not cls.__isinstance:
                cls.__isinstance = Pocket()
            return cls.__isinstance

        @classmethod
        def getMoney(cls):
            return cls.money

        @classmethod
        def addMoney(cls, debet):
            cls.money += debet

        @classmethod
        def lendMoney(cls, credit):
            if cls.money < credit:
                raise MoneyError
            cls.money -= credit
            return credit

 
