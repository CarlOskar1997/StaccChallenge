import json
import random

class Bank:
    with open("accounts.json") as data_acc:
        accounts_JSON = json.load(data_acc)
    with open("transactions.json") as data_trx:
        transactions_JSON = json.load(data_trx)
    accounts = accounts_JSON.get("accounts")
    milestones = {"low":100,
                  "medium":100000,
                  "high":1000000}
    def __init__(self):
        pass
    def userlist(self):
        print(self.accounts)
    def register_user(self, id, account_number, account_type, balance, currency, owner):
        x = {'id': id,
             'account_number':account_number,
             'account_type':account_type,
             'balance': balance,
             'currency':currency,
             'owner':owner}
        self.accounts.append(x)
        self.accounts_JSON.update({"accounts":self.accounts})
        print(self.accounts_JSON)
        with open("accounts.json", 'w') as json_file:
            json.dump(self.accounts_JSON, json_file, 
                        indent=4,  
                        separators=(',',': '))
    '''def set_milestone_check(self, milestone):
        for i in self.accounts:'''

            
    def annual_savings_check(self):
        for i in self.accounts:
            if i.get("account_type") == "Checking" and i.get("balance") >= self.milestones.get("low"):
                print("Congratulations!!!!")

        




test = Bank()
test.annual_savings_check()
#test.register_user('xyz123', '**********123', 'Checking', 1000000, 'NOK', 'Carl')