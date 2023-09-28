    def save_distances(self, filename, genome_list):
        """Save the generated distances to a text file"""
        with open(filename, 'w') as file:
            for bee_index, (_, bee_distance) in enumerate(genome_list, start=1):
                file.write(f"Bee {bee_index} total distance: {bee_distance}\n")



    for bee_index, (bee_genome, bee_distance) in enumerate(genome_list, start=1):
        print(f"Bee {bee_index} genome:")
        for flower_index, flower in enumerate(bee_genome, start=1):
            print(f"  Flower {flower_index}: ({flower.x}, {flower.y})")
        print(f"Bee {bee_index} total distance: {bee_distance}")
        print()

    beehive.save_distances("bee_distance.txt", genome_list)
    
        available_parents = Beehive(0, 0, flowers)
        for bee in Beehive:
            parent_a = random.sample(available_parents)
            available_parents.remove(parent_a)
            parent_b = random.sample(available_parents)
            available_parents.remove(parent_b)
            # pivot is 1/3 of parent A and 2/3 of parent B for 1st child
            # pivot is 2/3 of parent A and 1/3 of parent B for 2nd child
            pivot = len(Beehive) // 3
            child1 = parent_a[0:pivot] + parent_b[pivot:len(Beehive)]
            child2 = parent_a[pivot:len(Beehive)] + parent_b[0:pivot]
            
            # Printing parents and children genome_list
            print("Parent A:", parent_a.genome_list)
            print("Parent B:", parent_b.genome_list)
            print("Child 1:", child1.genome_list)
            print("Child 2:", child2.genome_list)
            
            
        def selection(self):
        removed_bees = []
        for bee_genome, bee_distance in self.genome_list:
            if bee_distance > sum(distance for _, distance in self.genome_list) / 2:
                removed_bees.append((bee_genome, bee_distance))

        for removed_bee in removed_bees:
            self.genome_list.remove(removed_bee)

        print("Genome List of Removed Bees:")
        for genome, distance in removed_bees:
            print(f"Genome: {genome}, Distance: {distance}")
                
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

        print("Genome List of Parents and Children:")
        for genome, distance in self.genome_list:
            print(f"Genome: {genome}, Distance: {distance}")
