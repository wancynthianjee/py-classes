class Account():
    bank="Stanbic"
    def __init__(self,withdraw,account_name,account_balance,print_statement,check_balance,transaction,loan_balance,borrow_loan):
        self.withdraw=[]
        self.deposit=[]
        self.loan_balance=0
        self.account_name=account_name
        self.account_balance=account_balance
        self.print_statement=print_statement
        self.transaction=transaction
        
        self.borrow_loan=borrow_loan
        self.check_balance=check_balance
    def show_owner(self):
        return f'{self.account_name}'
    def show_balance(self):
        return f'{self.account_balance}'
    def withdraw_money(self):
        return  {self.account_balance} - {self.withdraw}

    def print_statement(self):
        all_transactions = self.deposit + self.withdrawal
        for transaction in all_transactions:
        return f"{transaction['narration']} - {transaction['amount']}"

    def borrow_loan(self, amount):
    if self.loan_balance > 0:
        return "You have an outstanding loan."
    elif amount <= 100:
        return "Sorry, the amount is not enough for withdrawal."
    def check_balance(self):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        total_withdrawals = sum(transaction["amount"] for transaction in self.withdrawals)
        current_balance = total_deposits - total_withdrawals
        return current_balance
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.account_balance += amount - self.loan_balance
            self.loan_balance = 0
        else:
            self.loan_balance -= amount
   
     def transfer(self, amount, account):
        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
            return f"Transferred {amount} to the account with balance {account.balance}"
        else:
            return f"Insufficient balance to transfer"


