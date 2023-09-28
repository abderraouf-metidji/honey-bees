import random
from main import *

class Beehive(Flower):
    def __init__(self, x, y, flowers):
        super().__init__(x, y)
        self.flowers = flowers
        self.distance_matrix = self.matrix()  # Calculate the distance matrix

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
        # if a bee's distance is in the second half then it is removed from the Beehive
        # the remaining bees are used for reproduction
        # print the genome_list of the bees that were removed
        pass
                
    def reproduction(self):
        """Reproduction of the bees that were kept in the Beehive"""
        # create a list of available parents from the 50 bees that were not removed
        # randomly select 2 parents from the list
        # create 2 children from the 2 parents
        # children are based on 1/3 of parent A and 2/3 of parent B for 1st child
        # children are based on 2/3 of parent A and 1/3 of parent B for 2nd child
        # add the 2 children to the Beehive
        # repeat until the Beehive has 100 bees again
        # print the genome_list of the parents and children
        pass
    
    def mutation(self):
        # pick a random bee from the Beehive and change its genome_list
        # the bee is picked based on a chance of 1/500
        # inverse the position of 2 flowers in the genome_list to reduce the total distance
        # print the genome_list of the bee that was mutated
        pass


if __name__ == '__main__':
    flower = Flower(0, 0)
    flowers = flower.flower_distance()
    beehive = Beehive(0, 0, flowers)
    genome_list = beehive.butiner(100)
    