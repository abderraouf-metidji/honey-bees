from random import choice
import random
import csv

class Flower:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.flowers = []

    def distance(self, other_flower):
        """Calculate distance between two flowers"""
        return ((float(self.x) - float(other_flower.x))**2 + (float(self.y) - float(other_flower.y))**2)**0.5

    def flower_distance(self):
        """Calculate distance between all flowers"""
        flowers = []
        with open('flower_coordinates.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                x, y = row[0], row[1]
                flowers.append(Flower(float(x), float(y)))  # Convert x and y to floats
        self.flowers = flowers  # Assign the list of flowers to self.flowers

        return flowers

    def matrix(self):
        """Create a matrix with all distances between flowers"""
        distance_matrix = [[flower.distance(other_flower) for other_flower in self.flowers] for flower in self.flowers]
        return distance_matrix

    # def print_matrix(self):
    #     """Print the matrix"""
    #     distance_matrix = self.matrix()
    #     for row in distance_matrix:
    #         rounded_row = [round(element, 1) for element in row]  # Round each element in the row
    #         print(rounded_row)

class Beehive(Flower):
    def __init__(self, x, y, flowers):
        super().__init__(x, y)
        self.flowers = flowers
        self.distance_matrix = self.matrix()  # Calculate the distance matrix
        self.genome_list = self.butiner(101)  # Create a list of 100 bees

    def butiner(self, num_iterations):
        """Managing the foraging of the bees"""
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
        self.genome_list.sort(key=lambda x: x[1])  # Sort the list by distance
        self.genome_list = self.genome_list[:50]  # Keep the 50 best bees

    def reproduction(self):
        # Create a list of available parents from the 50 bees that were not removed
        available_parents = self.genome_list[:50]

        # Check if there are enough available parents to perform reproduction
        while len(self.genome_list) < 100 and len(available_parents) >= 2:
            # Randomly select 2 parents from the list
            parent_a = choice(available_parents)
            available_parents.remove(parent_a)

            # Filter available parents that don't have the same flower in their genome list
            valid_parents = [parent for parent in available_parents if not any(flower in parent[0] for flower in parent_a[0])]
            if not valid_parents:
                break  # Break the loop if there are no valid parents remaining

            parent_b = choice(valid_parents)
            available_parents.remove(parent_b)

            # Calculate the pivot point
            pivot = len(parent_a[0]) // 3

            # Create children based on the pivot
            child1_genome = parent_a[0][:pivot] + parent_b[0][pivot:]
            child2_genome = parent_b[0][:pivot] + parent_a[0][pivot:]

            # Calculate the distances for the children
            child1_distance = self.calculate_distance(child1_genome)
            child2_distance = self.calculate_distance(child2_genome)

            # Add the children to the Beehive
            self.genome_list.append((child1_genome, child1_distance))
            self.genome_list.append((child2_genome, child2_distance))

            
    # def print_genome_list(self):
    #     count = 0
    #     for genome, distance in self.genome_list:
    #         count += 1
    #         flower_coordinates = [(flower.x, flower.y) for flower in genome]
    #         print(f'Bee {count} - Distance: {distance}')

    def calculate_distance(self, genome):
        """Calculate the distance for a given genome"""
        distance = 0
        for i in range(1, len(genome)):
            prev_flower = genome[i - 1]
            curr_flower = genome[i]
            distance += self.distance_matrix[self.flowers.index(prev_flower)][self.flowers.index(curr_flower)]
        return distance


# if __name__ == '__main__':
    # flower = Flower(0, 0)
    # flowers = flower.flower_distance()
    # beehive = Beehive(0, 0, flowers)
    # beehive.selection()
    # beehive.reproduction()
    # flower.print_matrix()
    # beehive.print_genome_list()