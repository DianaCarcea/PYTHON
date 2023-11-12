class Account:
    def __init__(self, nr_cont, sold, moneda):
        self._nr_cont = nr_cont
        self._sold = sold
        if moneda not in {"USD", "EUR", "GBP", "AUD", "JPY", "RON", "RUB"}:
            raise ValueError("Moneda nevalidă!")
        self._moneda = moneda

    def deposit(self, suma):
        if suma <= 0:
            raise ValueError("Suma de depunere trebuie sa fie pozitiva!")
        self._sold = self._sold + suma

    def withdraw(self, suma):
        if suma <= 0:
            raise ValueError("Suma de retragere nevalida!")
        if suma > self._sold:
            raise ValueError("Fonduri insuficiente!")
        self._sold = self._sold - suma

    def get_info_cont(self):
        return self._nr_cont, self._sold, self._moneda

    def interest_calculation(self):
        pass


class SavingsAccount(Account):
    def __init__(self, nr_cont, sold=0, moneda="USD", rata_dobanda=0.01):
        super().__init__(nr_cont, sold, moneda)

        if not 0 < rata_dobanda < 1:
            raise ValueError("Rata dobanzii trebuie să fie in intervalul (0,1)!")

        self._rata_dobanda = rata_dobanda

    def interest_calculation(self):
        dobanda = self._sold * self._rata_dobanda  #dobanda=sold actual * rata dobanda
        self.deposit(dobanda)


class CheckingAccount(Account):
    def __init__(self, nr_cont, sold=0, moneda="USD", limita_descoperire=200):
        super().__init__(nr_cont, sold, moneda)
        self.limita_descoperire = limita_descoperire

    def withdraw(self, suma):
        if suma <= 0:
            raise ValueError("Suma de retragere nevalida!")
        if suma > (self._sold + self.limita_descoperire):
            raise ValueError("Retragere nereusita, se depaseste sold + limita descoperire")
        self._sold = self._sold - suma


if __name__ == '__main__':
    print("-------Saving-------")
    savings_account = SavingsAccount(nr_cont="CD125", sold=1000, moneda="EUR", rata_dobanda=0.02)
    print(f"Cont: {savings_account.get_info_cont()[0]}")
    print(f"Sold curent: {savings_account.get_info_cont()[1]} {savings_account.get_info_cont()[2]}")
    savings_account.deposit(500)
    print(f"Sold cu depunere: {savings_account.get_info_cont()[1]} {savings_account.get_info_cont()[2]}")
    savings_account.interest_calculation()
    print(f"Sold cu dobanda: {savings_account.get_info_cont()[1]} {savings_account.get_info_cont()[2]}")
    savings_account.withdraw(300)
    print(f"Sold cu retragere: {savings_account.get_info_cont()[1]} {savings_account.get_info_cont()[2]}")

    print("\n-------Checking-------")
    checking_account = CheckingAccount(nr_cont="CM118", sold=700, moneda="GBP", limita_descoperire=300)
    print(f"Cont: {checking_account.get_info_cont()[0]}")
    print(f"Sold curent: {checking_account.get_info_cont()[1]} {checking_account.get_info_cont()[2]}")
    checking_account.deposit(250)
    print(f"Sold cu depunere: {checking_account.get_info_cont()[1]} {checking_account.get_info_cont()[2]}")
    checking_account.withdraw(500)
    print(f"Sold cu retragere: {checking_account.get_info_cont()[1]} {checking_account.get_info_cont()[2]}")
