class persegi_panjang:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def keliling (self):
        return 2*(self.x + self.y)
    def luas (self):
        return self.x * self.y
    def __str__ (self):
        return (f"persegi_panjang, panjang{self.x}cm , lebar{self.y}cm")

def main ():
        try:
            x = int(input("enter the number:"))
            y = int(input("enter the number:"))
            pp = persegi_panjang (x, y)
            
            if x <= 0 or y <= 0:
                print("nilai tidak boleh nol atau minus, nilai tidak valid")
                return
            print(pp)
            print(f"keliling persegi panjang:{pp.keliling()} cm")
            print(f"luas persegi panjang:{pp.luas()} cm2")
        except ValueError:
            print("nilai tidak valid")
main()

    