# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Simple class definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(numbers)
    print("Sorted array:", numbers)

    my_car = Car("Toyota", "Corolla", 2020)
    my_car.display_info()