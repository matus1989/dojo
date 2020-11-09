

class Transfer:
    format_string = "%m-%d-%Y %H:%M:%S"
    def __init__(self,data,amount,balance):
       self.data = str(data)
       self.amount = str(amount)
       self.balance = str(balance)
    
    def __str__(self):
        return "Data: "+self.data + " Amount: "+ self.amount  + " Balance: "+self.balance