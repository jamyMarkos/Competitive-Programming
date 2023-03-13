class Bank:
    def __init__(self, balance: List[int]):
        self.bankList = [val for val in balance]
        self.num_acc = len(self.bankList)
        
    def isValid(self, acc_num) -> bool:
        return 0 < acc_num <= self.num_acc 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 < account1 <= self.num_acc and 0 < account2 <= self.num_acc:
            if self.bankList[account1 - 1] >= money:
                self.bankList[account2-1] += money
                self.bankList[account1 - 1] -= money
                return True
        return False
        
    def deposit(self, account: int, money: int) -> bool:
        if 0 < account <= self.num_acc:
            self.bankList[account - 1] += money
            return True
        return False
        
    def withdraw(self, account: int, money: int) -> bool:
        if 0 < account <= self.num_acc and self.bankList[account-1] >= money:
            self.bankList[account-1] -= money
            return True
        return False
            
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)