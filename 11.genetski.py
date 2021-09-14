import string
import random


#kako reprezentujemo jednu jedinku
class Chromosome:
    def __init__(self, genetic_code, fitness):
        self.genetic_code = genetic_code
        self.fitness = fitness

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{} = {}".format(''.join(self.genetic_code), self.fitness)


class GeneticAlgorithm:
    def __init__(self, possible_gene_values, target):
        print("Trying to guess: ", ''.join(target))
        self.possible_gene_values = possible_gene_values
        self.target = target

        self.max_iterations = 1000
        self.generation_size = 10
        self.chromosome_size = len(self.target)

    #1
    def initial_population(self):
        result = []
        for _ in range(self.generation_size):
            genetic_code = [random.choice(self.possible_gene_values) for _ in range(self.chromosome_size)]
            fitness = self.calculate_fitness(genetic_code)
            chromosome = Chromosome(genetic_code, fitness)
            result.append(chromosome)
        return result

    def calculate_fitness(self, genetic_code):
        fitness = 0
        for i in range(self.chromosome_size):
            if genetic_code[i] == self.target[i]:
                fitness += 1
        return fitness


    #2
    #def selection(self):


    #3
    #def create_generation(self):


    #4
    #def best_fit(self):
    

    def optimize(self):
        population = self.initial_population()
        print(population)
        return None 
        for _ in range(self.max_iterations):
            selected = self.selection(population)
            population = self.create_generation(selected)
            current_best = max(population, key = lambda x: x.fitness)

            if self.best_fit(current_best):
                result = current_best
                break
        
        return result


def get_random_string(n):
    return [random.choice(list(string.ascii_letters)) for _ in range(n)]


def main():
    genetic_algorithm = GeneticAlgorithm(string.ascii_letters, get_random_string(10))
    result = genetic_algorithm.optimize()
    print(result)


if __name__ == "__main__":
    main()
