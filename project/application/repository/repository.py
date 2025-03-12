from application.entities.entities import Masina


class MasinaRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__cars = self.load_data()

    def load_data(self):
        cars = []
        with open(self.__file_name, 'r') as f:
            for line in f:
                mas = line.split(' ')
                masina = Masina(mas[0], mas[1], mas[2], int(mas[3]), int(mas[4]))
                cars.append(masina)
        return cars

    def find(self, token):
        for car in self.__cars:
            if car.token_masina == token:
                return car

    def find_all(self):
        return self.__cars
