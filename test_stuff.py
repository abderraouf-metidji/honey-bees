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