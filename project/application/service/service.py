class MasinaService:
    def __init__(self, masina_repository):
        self.__masina_repository = masina_repository

    def find(self, token):
        return self.__masina_repository.find(token)

    # Sort by token
    def sort_by_token(self):
        return sorted(self.__masina_repository.find_all(), key=lambda masina: masina.token_masina)

    # Sort by marca & model
    def sort_by_marca_model(self):
        return sorted(self.__masina_repository.find_all(), key=lambda masina: (masina.marca, masina.model))

    # Sort by marca, model & token
    def sort_by_marca_model_token(self):
        cars = self.__masina_repository.find_all()
        return sorted(cars, key=lambda masina: (masina.marca, masina.model, masina.token_masina))

    # Sort by profit (pret_vanzare - pret_achizitie)
    def sort_by_profit(self):
        cars = self.__masina_repository.find_all()
        return sorted(cars, key=lambda masina: masina.pret_vanzare - masina.pret_achizitie)
