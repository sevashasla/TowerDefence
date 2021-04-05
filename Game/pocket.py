<<<<<<< HEAD
from .errors import MoneyError

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
=======
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
>>>>>>> delete it later
            if cls.money < credit:
                raise MoneyError
            cls.money -= credit
            return credit

 
