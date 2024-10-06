class User :
    #Constructor
    def __init__(self, name, age, gender, nik):
        self._name = name
        self._age = age
        self._gender = gender
        self._nik = nik
    #getter n setter
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def get_age(self):
        return self._age
    def set_age(self, value):
        self._age = value
    def get_gender(self):
        return self._gender
    def set_gender(self, value):
        self._gender = value
    def get_nik(self):
        return self._nik
    def set_nik(self, value):
        self._nik = value
    #method
    def print(self):
        print("=== DATA DIRI ===")
        print(f"Nama/NIK : {self._name}/{self._nik}")
        print(f"Umur : {self._age}")
        print(f"Jenis Kelamin: {self._gender}")

    def update_data(self):
        pass
