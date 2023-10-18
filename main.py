from beehive import * 
import random

class Generation(Beehive):
    def __init__(self, x, y, flowers):
        super().__init__(x, y, flowers)
        
        generation = 0
        avg_distances = []
        
        while generation < 10:
            self.genome_list = self.butiner(101)
            self.genome_list.sort(key=lambda x: x[1])
            self.genome_list = self.genome_list[:100]
            generation += 1
            
            avg_distance = sum(distance for _, distance in self.genome_list) / len(self.genome_list)
            avg_distances.append(avg_distance)
            
            print(f"Generation {generation}: Average distance: {avg_distance}")

    def print_genome_list(self):
        count = 0
        for genome, distance in self.genome_list:
            count += 1
            flower_coordinates = [(flower.x, flower.y) for flower in genome]
            print(f'Bee {count} - Distance: {distance}')

if __name__ == '__main__':
    flower = Flower(0, 0)
    flowers = flower.flower_distance()
    generation = Generation(0, 0, flowers)
    generation.print_genome_list()
