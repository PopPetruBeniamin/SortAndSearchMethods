from application.repository.repository import MasinaRepository


# ========== Search algorithm linear ==================================================================================

def search_alg_linear(cars, criteria, val):
    for car in cars:
        if comparator(car, criteria, val) == 0:
            return car
    return -1


# ========== Search algorithm binary ==================================================================================

def search_alg_binary(cars, criteria, val):
    low = 0
    high = len(cars) - 1

    while low <= high:
        mid = (high + low) // 2
        if comparator(cars[mid], criteria, val) == 1:
            high = mid - 1
        elif comparator(cars[mid], criteria, val) == -1:
            low = mid + 1
        else:
            return cars[mid]

    return None


# ========== Sorts the list by criteria ===============================================================================

def sorted_by_criteria(cars, criteria):
    # Sort the list based on the specified criteria
    match criteria:
        case 'marca':
            return sorted(cars, key=lambda car: car.marca)
        case 'model':
            return sorted(cars, key=lambda car: car.model)
        case 'token_masina':
            return sorted(cars, key=lambda car: car.token_masina)
        case 'pret_achizitie':
            return sorted(cars, key=lambda car: car.pret_achizitie)
        case 'pret_vanzare':
            return sorted(cars, key=lambda car: car.pret_vanzare)


# ================= Compares two cars based on a specific criteria ===================================================

def comparator(car, criteria, val):
    match criteria:
        case 'marca':
            return 1 if car.marca > val else -1 if car.marca < val else 0
        case 'model':
            return 1 if car.model > val else -1 if car.model < val else 0
        case 'token_masina':
            return 1 if car.token_masina > val else -1 if car.token_masina < val else 0
        case 'pret_achizitie':
            return 1 if car.pret_achizitie > val else -1 if car.pret_achizitie < val else 0
        case 'pret_vanzare':
            return 1 if car.pret_vanzare > val else -1 if car.pret_vanzare < val else 0


# ========== Running all functions ===================================================================================

lst = MasinaRepository(file_name="data/data").find_all()

print("Linear search: ")
print(search_alg_linear(lst, 'marca', 'Ford'))

print("\nBinary search: ")
lst = sorted_by_criteria(lst, 'marca')
print(search_alg_binary(lst, 'marca', 'Ford'))
