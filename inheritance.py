class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.account_balance: account_balance
        self.phone_number: phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"KES {amount} sent to {recipient} successfully!")
        else:
            print("You have insufficient funds to complete the transaction.")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"You have successfully bought airtime worth KES {amount}")
        else:
            print("You have insufficient funds to complete the transaction.")



class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
    def receive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} has been received from customer.")

personal=PersonalMpesa(150,78888,11111)
personal.send_money(300,69)
personal.buy_airtime(150)

business=BusinessMpesa(15000,787878,"91E")
business.receive_payment(8900)
business.send_money(8900,787878)
