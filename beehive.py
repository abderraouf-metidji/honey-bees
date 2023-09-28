import random
from main import *

class Beehive(Flower):
    def __init__(self, x, y, flowers):
        super().__init__(x, y)
        self.flowers = flowers
        self.distance_matrix = self.matrix()  # Calculate the distance matrix
        self.genome_list = self.butiner(100)  # Create a list of 100 bees

    def butiner(self, num_iterations):
        """Managing the foraging of the bees"""
        genome_list = []

        for _ in range(num_iterations):
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
        removed_bees = []
        for bee_genome, bee_distance in self.genome_list:
            if bee_distance > sum(distance for _, distance in self.genome_list) / 100:
                removed_bees.append((bee_genome, bee_distance))

        for removed_bee in removed_bees:
            self.genome_list.remove(removed_bee)

        # print("Genome List of Removed Bees:")
        # for genome, distance in removed_bees:
        #     print(f"Genome: {genome}, Distance: {distance}")
                
    def reproduction(self):
        # Create a list of available parents from the 50 bees that were not removed
        available_parents = self.genome_list[:50]

        # Check if there are enough available parents to perform reproduction
        while len(self.genome_list) < 100 and len(available_parents) >= 2:
            # Randomly select 2 parents from the list
            parent_a = random.choice(available_parents)
            available_parents.remove(parent_a)
            parent_b = random.choice(available_parents)
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

        # print("Genome List of Parents and Children:")
        # for genome, distance in self.genome_list:
        #     print(f"Genome: {genome}, Distance: {distance}")
        
    def mutation(self):
        pass

if __name__ == '__main__':
    flower = Flower(0, 0)
    flowers = flower.flower_distance()
    beehive = Beehive(0, 0, flowers)
    beehive.selection()
    beehive.reproduction()