#继承
class User:
    def method(self):
        pass
class Father:
    def eat(self):
        print("eat")
    def sleep(self):
        print("sleep...")
class Boys(Father,User):
    def playGame(self):
        print("game...")
class Grils(Father):
    def shopping(self):
        print("shopping...")
jack = Boys()
jack.eat()


