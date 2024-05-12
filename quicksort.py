from manim import *


class QuickSort(Scene):
    def construct(self):
        # Create a list of numbers to sort
        numbers = [5, 2, 8, 3, 1, 6, 4]

        # Create a bar chart to visualize the list
        bars = VGroup(*[Rectangle(width=1, height=n, fill_opacity=0.5)
                      for n in numbers])
        bars.arrange(RIGHT, buff=0.1)
        self.add(bars)

        # Define the quicksort function
        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                self.wait(0.5)
                quicksort(arr, low, pi-1)
                self.wait(0.5)
                quicksort(arr, pi+1, high)

        # Define the partition function
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self.wait(0.1)
                    self.play(
                        bars[i].animate.set_height(arr[i]),
                        bars[j].animate.set_height(arr[j])
                    )
            arr[i+1], arr[high] = arr[high], arr[i+1]
            self.wait(0.1)
            self.play(
                bars[i+1].animate.set_height(arr[i+1]),
                bars[high].animate.set_height(arr[high])
            )
            return i + 1

        # Call the quicksort function
        quicksort(numbers, 0, len(numbers)-1)

        # Wait for a bit before ending the scene
        self.wait(2)


# Create the scene and render it
scene = QuickSort()
scene.render()
