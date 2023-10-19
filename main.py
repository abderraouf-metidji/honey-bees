import os
from beehive import Flower, Beehive
import statistics
import matplotlib.pyplot as plt

class Generation(Beehive):
    def __init__(self, x, y, flowers, num_generations=25):
        """
        Initializes a new generation of bees.
        """
        super().__init__(x, y, flowers)
        self.avg_distances = []
        self.generation = 0
        self.genome_list = []

        while self.generation < num_generations:
            if self.generation == 0:
                self.genome_list = self.butiner(100)  
            else:
                self.selection()
                self.reproduction()

            self.generation += 1
            avg_distance = round(statistics.mean(distance for _, distance in self.genome_list), 2)
            self.avg_distances.append(avg_distance)
            print("Generation {}: Average distance: {}".format(self.generation, avg_distance))

    def save_graphs(self):
        """
        Saves the best bee path and average distance evolution graphs.
        Creates a 'graphs' folder if it doesn't exist and saves the graphs in that folder.
        """
        if not os.path.exists('graphs'):
            os.makedirs('graphs')

        best_bee_genome, _ = min(self.genome_list, key=lambda x: x[1])
        x_values = [flower.x for flower in best_bee_genome]
        y_values = [flower.y for flower in best_bee_genome]

        plt.figure()
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
        plt.plot(x_values[0], y_values[0], marker='o', color='g')  # Starting point in green
        plt.plot(x_values[-1], y_values[-1], marker='o', color='r')  # Ending point in red
        plt.title('Best Bee Path')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('graphs/best_bee_path.png')
        plt.show()

        plt.figure()
        plt.plot(range(1, len(self.avg_distances) + 1), self.avg_distances, marker='o', linestyle='-', color='r')
        plt.title('Evolution of Average Distance')
        plt.xlabel('Generation')
        plt.ylabel('Average Distance')
        plt.savefig('graphs/average_distance_evolution.png')
        plt.show()

if __name__ == '__main__':
    flower = Flower(0, 0)
    flowers = flower.flower_distance()
    generation = Generation(0, 0, flowers)
    generation.save_graphs()