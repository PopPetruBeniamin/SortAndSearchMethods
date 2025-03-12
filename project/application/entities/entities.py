class Masina:
    def __init__(self, marca, model, token_masina, pret_achizitie, pret_vanzare):
        self.__marca = marca
        self.__model = model
        self.__token_masina = token_masina
        self.__pret_achizitie = pret_achizitie
        self.__pret_vanzare = pret_vanzare

    def __str__(self):
        return (f"Masina: Marca: {self.__marca}, Model: {self.__model}, Token masina: {self.__token_masina}, "
                f"Pret achizitie: {self.__pret_achizitie}, Pret vanzare: {self.__pret_vanzare}")

    # Getters
    @property
    def marca(self):
        return self.__marca

    @property
    def model(self):
        return self.__model

    @property
    def token_masina(self):
        return self.__token_masina

    @property
    def pret_achizitie(self):
        return self.__pret_achizitie

    @property
    def pret_vanzare(self):
        return self.__pret_vanzare
