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
                flowers.append(Flower(float(x), float(y)))
        self.flowers = flowers
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
        self.distance_matrix = self.matrix()  

    def butiner(self, num_iterations):
        """
        Manages the foraging behavior of the bees.
        Returns:
            list: A list of tuples representing the genomes and distances traveled by the bees.
        """
        genome_list = []
        for _ in range(num_iterations):
            remaining_flowers = self.flowers.copy()
            bee_genome = []
            bee_distance = 0
            while remaining_flowers:
                random_flower = random.choice(remaining_flowers)  
                bee_genome.append(random_flower)
                
                if len(bee_genome) > 1:
                    prev_flower = bee_genome[-2]
                    bee_distance += self.distance_matrix[self.flowers.index(prev_flower)][self.flowers.index(random_flower)]
                remaining_flowers.remove(random_flower)  
            genome_list.append((bee_genome, bee_distance))
        return genome_list

    def selection(self):
        """
        Selects the best-performing bees based on the distance traveled.
        Returns:
            list: The list of the best-performing bees.
        """
        self.genome_list.sort(key=lambda x: x[1])  
        self.genome_list = self.genome_list[:50] 
        return self.genome_list

    def reproduction(self):
        """
        Performs reproduction by creating offspring from the selected parents.
        Returns:
            list: The updated list of genomes after reproduction.
        """
        available_parents = self.genome_list.copy()
        while len(self.genome_list) < 100 and len(available_parents) >= 2:  
            parent_a = choice(available_parents)  
            available_parents.remove(parent_a)
            parent_b = choice(available_parents)
            available_parents.remove(parent_b)
            pivot = len(parent_a[0]) // 4  
            child1_genome = parent_a[0][:pivot] + parent_b[0][pivot:] 
            child2_genome = parent_b[0][:pivot] + parent_a[0][pivot:]
            child1_distance = self.calculate_distance(child1_genome)  
            child2_distance = self.calculate_distance(child2_genome)
            if len(self.genome_list) < 100: 
                self.genome_list.append((child1_genome, child1_distance))
            if len(self.genome_list) < 100:  
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