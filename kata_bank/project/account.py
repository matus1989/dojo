from transfer import Transfer
from string import Template
from datetime import date, time, datetime

class Account:
    format_string = "%m-%d-%Y %H:%M:%S"

    def __init__(self, balance):
        self.transfer = []
        self.balance = balance

    def deposite(self, amount):
        if self.__check_type(amount):
            self.balance =self.balance + amount
            self.add_transfer_log(str(amount))


    def withdraw(self,amount):
        if self.__check_type(amount):
            self.balance = self.balance - amount
            self.add_transfer_log("-"+str(amount))


    def add_transfer_log(self,amount):
        trans = Transfer(datetime.now().strftime(self.format_string), amount, self.balance)
        self.transfer.append(trans)

    def print_transaction(self):
        for trans in self.transfer:
            print (trans)

    def __check_type(self, amount):
        if type(amount) is int:
            return True
        else:
            raise TypeError(Template("Wrong type. Should be int and it's $value").substitute(value=amount))


if __name__ == "__main__":
    acc = Account(500)
    acc.deposite(1000)
    acc.withdraw(400)
    acc.print_transaction()