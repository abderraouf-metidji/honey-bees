
# Honey and bees

Project done using : 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Project

The project is focused on a genetic algorithm that will allow the creation and management of a beehive and its evolution throughout multiple generations.

The goal is to reach a bee generation that will go through the 50 available flowers using the shortest path possible. 

## Solution and implementation

The algorithm is focused around core methods that are:
* Forager
* Selection
* Reproduction

The **forager** method is used only once in the algorithm and its main goal is to create the first generation of bees using randomly generated bees and their foraging routes.

The second method **selection** is used to select, out of the 100 bees, the 50 fastest bees by simply sorting the average distance from lowest to highest and taking the first 50 bees in the list.

The third and last core method is the **reproduction** method which is simply used to manage the creation of new bees using the **genome list** of the 50 remaining bees.

The **genome list** is a list of list containing the list of flowers the bee has traveled to and the distance the bee has traveled.

Other methods used are mainly for checking the number of flowers in each bee genome list, checking for duplicate flowers and the management of the mutation strategy. 

### Without checking for duplicates

The first test case will be by using an algorithm that doesn't check for the number of flowers in each genome list, doesn't check for duplicates and has no mutation strategy.

[![Image](https://i.goopics.net/fnasg7.png)](https://goopics.net/i/fnasg7)

What we can see on the graph is that the average distance for each generation does go down gradually but it stagnates quite fast (around the generation 8/11 on average) and is then stuck around 18,000 to 20,000 average distance. 

### While checking for duplicates

For the second test case I have introduced two new methods that will:
* Check the number of flowers in each bee genome list twice, the first time when the first generation has been created and the second time when the **reproduction** method is used to create 50 new bees
* Check if there are duplicate flowers in each bee genome list

With these methods we are able to ensure that each bee visits 50 flowers each time and that there are 50 unique flowers in each bee genome list.

[![Image](https://i.goopics.net/hnm4sc.png)](https://goopics.net/i/hnm4sc)

As we can see with the graph below it has helped with lowering the average distance quite a bit. We are now averaging 13,000 to 14,000 instead of 18,000 to 20,000.

### With mutation strategy

Now that we are averaging a lower distance per generation we will be introducing a mutation strategy.

The mutation method used here is quite simple, we are triggering a mutation when the average distance stays the same for 5 generations. The **mutation** method then takes a random bee out of the 100 and switches two random flowers in the genome list. 

This is mainly used to get out of stagnation by introducing a new variable. 
[![Image](https://i.goopics.net/cv8vuw.png)](https://goopics.net/i/cv8vuw)

Of course, as we can see with the graph the stagnation is still quite present but we manage to lower the average distance.
Here we are managing to get to  10,000 ~ 11,000 with 2000 generations.

## Conclusion

In conclusion, the genetic algorithm developed for the management and optimization of the beehive has demonstrated promising results, particularly in terms of improving the efficiency of bee foraging routes. Through systematic implementation and careful consideration of various methods such as **forager**, **selection**, **reproduction**, and the introduction of checks for duplicates and a mutation strategy, the algorithm has shown a significant reduction in the average distance traveled by bees over multiple generations.

Other mutation strategies are available, such as the use of a method that switches the place of two flowers by taking into account the average distance and always switching two flowers that will lower that distance, but we opted to use a simple random method. The introduction of this mutation strategy, triggered to overcome stagnation, has further contributed to the algorithm's ability to continuously optimize bee behavior and enhance overall performance. 


