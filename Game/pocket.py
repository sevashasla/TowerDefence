class MoneyError(Exception):
    pass


class Pocket(object):

        money = 0

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.__instance = super(Pocket, cls).__new__(cls)
            return cls.__instance

        @classmethod
        def get_money(cls):
            return cls.money

        @classmethod
        def add_money(cls, debet):
            cls.money += debet

        @classmethod
        def lend_money(cls, credit):
            if cls.money < credit:
                raise MoneyError
            cls.money -= credit
            return credit

 
