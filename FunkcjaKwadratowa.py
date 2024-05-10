import math

class FunkacjaKwadratowa:
    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c
        self.funkcja =  str(a) + "x^2" + str(b) + "x" + str(c)

    def rozw (self):
        delta = pow(float(self.b), 2) - 4 *float(self.a) *float(self.c)
        print(self.a)
        print(delta)

        if delta > 0 and delta != 0:
            if float(self.a) != 0:
                pierwiastek_delta = math.sqrt(delta)
                print(pierwiastek_delta)
                miejsce_zerowe_1 =  (-float(self.b) +float(pierwiastek_delta))/(2*float(self.a))
                print(2*float(self.a))
                miejsce_zerowe_2 = (-float(self.b) - float(pierwiastek_delta))/(2*float(self.a))
                print("Twoje miejsca zerowe to:")
                print("x1= " + str(miejsce_zerowe_1))
                print("x2= " + str(miejsce_zerowe_2))
            else:
                miejsce_zerowe_1 = float(self.c)/float(self.b)
                print("Twoje miejsca zerowe to:")
                print("x1= " + miejsce_zerowe_1)
        elif delta == 0:
            pierwiastek_delta = math.sqrt(delta)
            miejsce_zerowe_1 = (float(self.b))/2*float(self.a)
            print("Twoje miejsca zerowe to:")
            print("x1= " + str(miejsce_zerowe_1))
        else:
            print("Twoja funkcja nie posiada miejsaca zerowego!")

a = input("Podaj parametr a: ")
b = input("Podaj parametr b: ")
c = input("Podaj parametr c: ")

funkcja = FunkacjaKwadratowa(a, b, c)
funkcja.rozw()
            
    