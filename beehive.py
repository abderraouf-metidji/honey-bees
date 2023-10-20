import csv
import random
from random import choice

class Flower:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.flowers = []

    def distance(self, other_flower):
        """
        Calculates the distance between two flowers.
        """
        return ((float(self.x) - float(other_flower.x))**2 + (float(self.y) - float(other_flower.y))**2)**0.5

    def flower_distance(self):
        """
        Reads the flower coordinates from a csv file and creates a list of Flower objects.
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
        Creates a distance matrix for all the flowers.
        """
        distance_matrix = [[flower.distance(other_flower) for other_flower in self.flowers] for flower in self.flowers]
        return distance_matrix

class Beehive(Flower):
    def __init__(self, x, y, flowers):
        super().__init__(x, y)
        self.flowers = flowers
        self.distance_matrix = self.matrix()  

    def forager(self, num_iterations):
        """
        Creates a list of bee genomes and their respective distances. This is for the first generation of bees.
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
        Selects the 50 best bees based on their distance traveled. The 50 bees with the lowest distance are selected.
        """
        self.genome_list.sort(key=lambda x: x[1])  
        self.genome_list = self.genome_list[:50] 
        return self.genome_list

    def reproduction(self):
        """
        Creates a new generation of bees by combining the genomes of the 50 best bees. 
        Two bees are selected at random and their genomes are combined to create two new bees.
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
        Uses the distance matrix to calculate the distance traveled by a bee.
        """
        distance = 0
        for i in range(1, len(genome)):
            prev_flower = genome[i - 1]
            curr_flower = genome[i]
            distance += self.distance_matrix[self.flowers.index(prev_flower)][self.flowers.index(curr_flower)]
        return distance
    
    def verify_flowers(self):
        """
        Checks if the bees have visited all the flowers. If not, the missing flowers are added to the bee's genome.
        """
        for i in range(len(self.genome_list)):
            bee_genome, _ = self.genome_list[i]
            if len(bee_genome) < 50:
                current_flowers = set(bee_genome)
                available_flowers = list(set(self.flowers) - current_flowers)
                while len(bee_genome) < 50:
                    new_flower = choice(available_flowers)
                    bee_genome.append(new_flower)
                    available_flowers.remove(new_flower)
            elif len(bee_genome) > 50:
                bee_genome = random.sample(bee_genome, 50)
            self.genome_list[i] = (bee_genome, self.calculate_distance(bee_genome))
            
    def verify_duplicate_flowers(self):
        """
        Checks if the bees have visited the same flower more than once. 
        If so, the duplicate flowers are removed and replaced with missing flowers.
        """
        for i in range(len(self.genome_list)):
            bee_genome, _ = self.genome_list[i]
            seen = set()
            missing_flowers = list(set(self.flowers) - set(bee_genome))
            for flower in bee_genome:
                if flower in seen:
                    bee_genome.remove(flower)
                    if missing_flowers:
                        new_flower = choice(missing_flowers)
                        bee_genome.append(new_flower)
                        missing_flowers.remove(new_flower)
                else:
                    seen.add(flower)
            while len(bee_genome) < 50 and missing_flowers:
                new_flower = choice(missing_flowers)
                bee_genome.append(new_flower)
                missing_flowers.remove(new_flower)
            self.genome_list[i] = (bee_genome, self.calculate_distance(bee_genome))