class Symbol:
    def __init__(self, sentence):
        self.name = sentence
        self.value = True
    
    def evaluate(self):
        return


class Not(Symbol):
    def __init__(self, symbol):
        super().__init__(symbol.name)
        self.symbol = symbol
        self.evaluate()
    
    def evaluate(self):
        self.symbol.evaluate()
        if self.symbol.value:
            self.value = False
        else:
            self.value = True



class And(Symbol):
    def __init__(self, *symbols):
        self.symbols = symbols
        tmpName = ""
        for i, symbol in enumerate(symbols):
            tmpName += symbol.name
            if(i < (len(symbols) - 1)):
                tmpName += " ^ "

        super().__init__(tmpName)
        self.evaluate()
    
    def evaluate(self):
        tmpValue = True
        for symbol in self.symbols:
            symbol.evaluate()
            tmpValue = tmpValue and symbol.value
        
        self.value = tmpValue


class Or(Symbol):
    def __init__(self, *symbols):
        self.symbols = symbols
        tmpName = ""
        for i, symbol in enumerate(symbols):
            tmpName += symbol.name
            if(i < (len(symbols) - 1)):
                tmpName += " ^ "

        super().__init__(tmpName)
        self.evaluate()
    
    def evaluate(self):
        tmpValue = False
        for symbol in self.symbols:
            symbol.evaluate()
            tmpValue = tmpValue or symbol.value
        
        self.value = tmpValue

class Implication(Symbol):
    def __init__(self, leftSymbol, rightSymbol):
        self.symbols = (leftSymbol, rightSymbol)
        tmpName = f"{leftSymbol.name} => {rightSymbol.name}"
        super().__init__(tmpName)
        self.evaluate()
    
    def evaluate(self):
        for i, symbol in enumerate(self.symbols):
            symbol.evaluate()
            if i == 0:
                l = symbol
            else:
                r = symbol
        
        if l.value and (not r.value):
            self.value = False
        else:
            self.value = True



def modelCheck(kb, target, symbols):
    length = len(symbols)
    x = 2 ** length
    kbCount = 0
    targetCount = 0
    for num in range(x):
        for i in range(length):
            v = bool(num & 1)
            num = num >> 1
            symbols[i].value = v
        
        kb.evaluate()

        if kb.value:
            kbCount += 1
            if target.value:
                targetCount += 1
            else:
                targetCount -= 1
        
    if (kbCount == targetCount):
        return 1
    elif (kbCount + targetCount == 0):
        return -1
    else:
        return 0






def main():
    rain = Symbol("it is rainning")
    hagrid = Symbol("hagrid")
    dumbledore = Symbol("dumbledore")

    knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
    )

    print(modelCheck(knowledge, rain, [rain, hagrid, dumbledore]))



if __name__ == "__main__":
    main()