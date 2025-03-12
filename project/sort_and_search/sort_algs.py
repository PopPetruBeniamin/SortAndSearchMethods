import time
import copy
from application.repository.repository import MasinaRepository


# ================= Compares two cars based on a specific attribute ===================================================
def comparator(car1, car2, comp):
    if comp == "token_masina":
        return car1 if car1.token_masina > car2.token_masina else car2
    elif comp == "marca":
        return car1 if car1.marca > car2.marca else car2
    elif comp == "model":
        return car1 if car1.model > car2.model else car2
    elif comp == "pret_achizitie":
        return car1 if car1.pret_achizitie > car2.pret_achizitie else car2
    elif comp == "pret_vanzare":
        return car1 if car1.pret_vanzare > car2.pret_vanzare else car2
    else:
        raise Exception(f"Invalid comparator: {comp}")


# ================= Bubble Sort (n^2) =================================================================================
def sort_alg_bubble(cars, comp):
    for i in range(0, len(cars)):
        for j in range(i + 1, len(cars)):
            if comparator(cars[i], cars[j], comp) == cars[i]:
                cars[i], cars[j] = cars[j], cars[i]


# ================= Quick Sort (n * log(n)) ===========================================================================
def partition(cars, comp, low, high):
    pivot = cars[high]
    i = low - 1
    for j in range(low, high):
        if comparator(cars[j], pivot, comp) == pivot:
            i = i + 1
            (cars[i], cars[j]) = (cars[j], cars[i])
    (cars[i + 1], cars[high]) = (cars[high], cars[i + 1])
    return i + 1


def sort_alg_quick(cars, comp, low, high):
    if low < high:
        pi = partition(cars, comp, low, high)
        sort_alg_quick(cars, comp, low, pi - 1)
        sort_alg_quick(cars, comp, pi + 1, high)


# ================== Calculates and writes data statistics for sorting algorithms time complexity =====================
def time_analysis():
    with open("data/big_data_time.txt", "w") as f:
        lst = MasinaRepository(file_name="data/big_data").find_all()
        old_lst = copy.deepcopy(lst)
        input_sizes = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000]

        f.write("Time Complexity for Bubble Sort (n^2) and Quick Sort (n * log(n))\n\n")
        f.write("n          Bubble Sort       Quick Sort           Difference\n")

        start_time = time.perf_counter()

        for size in input_sizes:
            # Calculate time for n^2
            lst = copy.deepcopy(old_lst)
            bubble_start = time.perf_counter()
            sort_alg_bubble(lst[:size], "pret_vanzare")
            bubble_end = time.perf_counter()
            bubble_time = (bubble_end - bubble_start)

            # Calculate time for n * log(n)
            lst = copy.deepcopy(old_lst)
            quick_start = time.perf_counter()
            sort_alg_quick(lst[:size], "pret_vanzare", 0, len(lst[:size]) - 1)
            quick_end = time.perf_counter()
            quick_time = (quick_end - quick_start)

            difference = int(bubble_time/quick_time)

            f.write(f"{size}           {bubble_time:.5f}s            {quick_time:.5f}s          x{difference} faster\n")

        end_time = time.perf_counter()
        f.write(f"\nCode run time: {int((end_time - start_time)/60)} minutes")


# ========== Running the function =====================================================================================

time_analysis()
