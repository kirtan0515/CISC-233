import random
import matplotlib.pyplot as plt

array_sizes = range(10, 100, 10)

bubble_steps = []
insertion_steps = []

for n in array_sizes:

    for _ in range(10000):
        arr = [random.randint(1, 100) for _ in range(n)]

        # Bubble Sort
        steps_bubble = 0

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                steps_bubble += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        bubble_steps.append(steps_bubble)

        # Insertion Sort
        steps_insertion = 0

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            steps_insertion += 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                steps_insertion += 1

            arr[j + 1] = key

        insertion_steps.append(steps_insertion)

# Plotting
plt.plot(bubble_steps, label='Bubble Sort')
plt.plot(insertion_steps, label='Insertion Sort')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('steps')
plt.title('Steps vs. Number of elements')

# Adding a legend
plt.legend()

# Display the plot
plt.show()

