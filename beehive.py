from random import choice
import random
import csv

class Flower:
    def __init__(self, x, y):
        """
        Initializes a Flower object with x and y coordinates.
        """
        self.x, self.y = x, y
        self.flowers = []

    def distance(self, other_flower):
        """
        Calculates the Euclidean distance between two flowers.
        """
        return ((float(self.x) - float(other_flower.x))**2 + (float(self.y) - float(other_flower.y))**2)**0.5

    def flower_distance(self):
        """
        Reads flower coordinates from a CSV file and creates a list of Flower objects.
        Returns:
            list: A list of Flower objects representing the flowers.
        """
        flowers = []
        with open('flower_coordinates.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                x, y = row[0], row[1]
                flowers.append(Flower(float(x), float(y)))  # Convert x and y to floats
        self.flowers = flowers  # Assign the list of flowers to self.flowers
        return flowers

    def matrix(self):
        """
        Creates a matrix with all distances between flowers.
        Returns:
            list: A matrix containing the distances between flowers.
        """
        distance_matrix = [[flower.distance(other_flower) for other_flower in self.flowers] for flower in self.flowers]
        return distance_matrix


class Beehive(Flower):
    def __init__(self, x, y, flowers):
        """
        Initializes a Beehive object with a position and a list of flowers.
        """
        super().__init__(x, y)
        self.flowers = flowers
        self.distance_matrix = self.matrix()  # Calculate the distance matrix
        self.genome_list = self.butiner(101)  # Create a list of 100 bees

    def butiner(self, num_iterations):
        """
        Manages the foraging behavior of the bees.
        Returns:
            list: A list of tuples representing the genomes and distances traveled by the bees.
        """
        genome_list = []
        for _ in range(num_iterations - 1):  # Run for num_iterations - 1 times to generate 100 genomes
            remaining_flowers = self.flowers.copy()  # Create a copy of the list of flowers
            bee_genome = []
            bee_distance = 0
            while remaining_flowers:
                random_flower = random.choice(remaining_flowers)  # Choose a random flower from the remaining ones
                bee_genome.append(random_flower)  # Add the random flower to the bee's genome list
                # Calculate the distance using the matrix
                if len(bee_genome) > 1:
                    prev_flower = bee_genome[-2]
                    bee_distance += self.distance_matrix[self.flowers.index(prev_flower)][self.flowers.index(random_flower)]
                remaining_flowers.remove(random_flower)  # Remove the chosen flower from the remaining flowers
            genome_list.append((bee_genome, bee_distance))
        return genome_list

    def selection(self):
        """
        Selects the best-performing bees based on the distance traveled.
        Returns:
            list: The list of the best-performing bees.
        """
        self.genome_list.sort(key=lambda x: x[1])  # Sort the list by distance
        self.genome_list = self.genome_list[:50]  # Keep the 50 best bees
        return self.genome_list

    def reproduction(self):
        """
        Performs reproduction by creating offspring from the selected parents.
        Returns:
            list: The updated list of genomes after reproduction.
        """
        available_parents = self.genome_list[:50]  # Create a list of available parents from the 50 bees that were not removed
        while len(self.genome_list) < 100 and len(available_parents) >= 2:  # Check if there are enough available parents to perform reproduction
            parent_a = choice(available_parents)  # Randomly select 2 parents from the list
            available_parents.remove(parent_a)
            parent_b = choice(available_parents)
            available_parents.remove(parent_b)
            pivot = len(parent_a[0]) // 2  # Calculate the pivot point
            child1_genome = parent_a[0][:pivot] + parent_b[0][pivot:]  # Create children based on the pivot
            child2_genome = parent_b[0][:pivot] + parent_a[0][pivot:]
            child1_distance = self.calculate_distance(child1_genome)  # Calculate the distances for the children
            child2_distance = self.calculate_distance(child2_genome)
            if len(self.genome_list) < 100:  # Check if the number of genomes is less than 100
                self.genome_list.append((child1_genome, child1_distance))
            if len(self.genome_list) < 100:  # Check if the number of genomes is less than 100
                self.genome_list.append((child2_genome, child2_distance))
        return self.genome_list

    def calculate_distance(self, genome):
        """
        Calculates the total distance traveled for a given genome.
        Returns:
            float: The total distance traveled by the bee.
        """
        distance = 0
        for i in range(1, len(genome)):
            prev_flower = genome[i - 1]
            curr_flower = genome[i]
            distance += self.distance_matrix[self.flowers.index(prev_flower)][self.flowers.index(curr_flower)]
        return distance