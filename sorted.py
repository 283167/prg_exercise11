import random
import matplotlib.pyplot as plt

def random_numbers(count, low = 0, high = 100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    for x in range(0, len(values)):
        min_index = x
        min_values = values[min_index]
        for i in range(x,len(values)):
            if values[i] < min_values:
                min_index = i
                min_values = values[i]
        values[x], values[min_index] = values[min_index], values[x]
    print(values)


def bubble_sort(values):
    result = values.copy()
    plt.ion()
    plt.show()
    for i in range(len(result)):
        swapped = False
        for x in range(1, len(result) - i):
            index_highlight1 = x - 1
            index_highlight2 = x
            colors = ["steelblue"] * len(result)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(result)), result, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.00000000000000000000000000000000001)
            if result[x-1] > result[x]:
                result[x-1], result[x] = result[x], result[x-1]
                swapped = True
        if swapped == False:
            return result
    plt.ioff()
    plt.show()
    return result

if __name__ == "__main__":
    values = random_numbers(100)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    #selection_sort(values)
    print(bubble_sort(values))
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)