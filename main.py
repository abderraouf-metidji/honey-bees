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

    def print_matrix(self):
        """Print the matrix"""
        distance_matrix = self.matrix()
        for row in distance_matrix:
            rounded_row = [round(element, 1) for element in row]  # Round each element in the row
            print(rounded_row)


if __name__ == '__main__':
    flower = Flower(0, 0)
    flower.flower_distance()
    flower.print_matrix()