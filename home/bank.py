class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):...

    def get_name(self):...

    def get_key(self):
        return self.__key
    def set_key(self, key):
        self.__key = key
    def get_money(self):
        return self.__money
    def set_money(self, money):
        self.__money = money

class Mbank(Bank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def set_name(self, name):
        self._name = name

class MiniMbank(Mbank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    @property
    def money(self):
        return self.get_money()
    @money.setter
    def money(self, money):
        self.set_money(money)
    @property
    def key(self):
        return self.get_key()
    @key.setter
    def key(self, key):
        self.set_key(key)
    
