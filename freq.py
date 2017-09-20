#DTMF KEYPAD FREQUENCIES

class Freq():
    def __init__(self):
        
        self.keypadF =[[1209, 1336, 1477, 1633],
                        [697, 770, 852, 941]]

        self.one = [self.keypadF[0][0],self.keypadF[1][0]]
        self.two = [self.keypadF[0][1],self.keypadF[1][0]]
        self.three = [self.keypadF[0][2],self.keypadF[1][0]]
        self.four = [self.keypadF[0][0],self.keypadF[1][1]]
        self.five = [self.keypadF[0][1],self.keypadF[1][1]]
        self.six = [self.keypadF[0][2],self.keypadF[1][1]]
        self.seven = [self.keypadF[0][0],self.keypadF[1][2]]
        self.eight = [self.keypadF[0][1],self.keypadF[1][2]]
        self.nine = [self.keypadF[0][2],self.keypadF[1][2]]
        self.zero = [self.keypadF[0][1],self.keypadF[1][3]]