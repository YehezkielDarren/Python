class Rekening:
    def __init__(self,saldo_awal,nama,no_rekening) -> None:
        self._no_rekening=no_rekening
        self._saldo=saldo_awal
        self._nama=nama
    def simpan_uang(self,setoran)-> None:
        if setoran>=0:
            self._saldo+=setoran
    def ambil_uang(self, penarikan)->None:
        if penarikan>0 and self._saldo>penarikan:
            self._saldo-=penarikan
            
if __name__=="__main__":
    pass