class Account():
    bank="Stanbic"
    def __init__(self,withdraw,account_name,account_balance):
        self.withdraw=withdraw
        self.account_name=account_name
        self.account_balance=account_balance
    def show_owner(self):
        return f'{self.account_name}'
    def show_balance(self):
        return f'{self.account_balance}'
    def withdraw_money(self):
        return  {self.account_balance} - {self.withdraw}
