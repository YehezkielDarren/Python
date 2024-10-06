import math
class PersegiPanjang:
    lebar=0.0
    panjang=0.0
    def luas(self):
        return self.panjang*self.lebar
    def keliling(self):
        return 2*(self.panjang+self.lebar) 
class Lingkaran:
    radius=0.0
    def luas(self):
        return math.pi*math.pow(self.radius,2)
    def keliling(self):
        return math.pi*(2*self.radius)

if __name__=="__main__":
    panjang=int(input("Panjang : "))
    lebar=int(input("Lebar : "))
    # Persegi Panjang
    p1=PersegiPanjang()
    p1.panjang=panjang
    p1.lebar=lebar
    luas=p1.luas()
    keliling=p1.keliling()
    print(f"Luas : {luas} cm*2\nKeliling : {keliling} cm")
    # Lingkaran
    radius=int(input("Radius Lingkaran : "))
    p2=Lingkaran()
    p2.radius=radius
    luas=p2.luas()
    keliling=p2.keliling()
    print(f"Luas : {luas} cm*2\nKeliling : {keliling} cm")