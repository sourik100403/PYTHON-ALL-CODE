class dad:
    tenis=1
class son(dad):
    football=2
    def func1(self):
        return f"i play game{self.football} and {self.tenis}"
class grandson(son):
    cricket=3
    dance=9
    def func2(self):
        return f" i have dance {self.dance} and {self.cricket} and football {self.football} and tenis {self.tenis}"
kajal=dad()
sourik=son()
konna=grandson()
print(kajal.tenis)
print(sourik.func1())
print(konna.func2())

