import math
import random


#kako reprezentujemo jednu jedinku
class Chromosome:
    def __init__(self, genetic_code, fitness):
        self.genetic_code = genetic_code
        self.fitness = fitness

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{} = {}".format(self.genetic_code, self.fitness)


class GeneticAlgorithm:
    def __init__(self):
        self.generation_size = 5000
        self.mutation_rate = 0.1
        self.reproduction_size = 1000
        self.max_iterations = 80
        self.chromosome_size = 4

    #1
    def initial_population(self):
        result = []
        for _ in range(self.generation_size):
            genetic_code = [random.uniform(-1, 1) for _ in range(self.chromosome_size)]
            fitness = self.calculate_fitness(genetic_code)
            chromosome = Chromosome(genetic_code, fitness)
            result.append(chromosome)
        return result

    def calculate_fitness(self, genetic_code):
        fitness = math.sin(genetic_code[0]) * (genetic_code[1]**2 - genetic_code[2]**3) * 20 + genetic_code[3] * genetic_code[0] - 2 * genetic_code[2]
        return fitness


    #2
    def selection(self, population):
        #turnirska
        '''result = []
        for _ in range(self.reproduction_size):
            sample = random.sample(population, 10)
            result.append(min(sample, key = lambda x: x.fitness))
        return result'''

        #ruletska
        selected = []
        for _ in range(self.reproduction_size):
            sample = random.choices(population, weights=[abs(x.fitness) for x in population], k=1)
            selected.append(sample[0])
        return selected


    #3
    def create_generation(self, selected):
        result = []
        for _ in range(self.generation_size // 2):
            parents = random.sample(selected, 2)

            child1_code, child2_code = self.crossover(parents[0], parents[1])

            child1_code = self.mutate(child1_code)
            child2_code = self.mutate(child2_code)

            child1 = Chromosome(child1_code, self.calculate_fitness(child1_code))
            child2 = Chromosome(child2_code, self.calculate_fitness(child2_code))

            result.append(child1)
            result.append(child2)
        return result

    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        break_point = random.randrange(self.chromosome_size)
        child1_code = parent1.genetic_code[:break_point] + parent2.genetic_code[break_point:]
        child2_code = parent2.genetic_code[:break_point] + parent1.genetic_code[break_point:]
        return child1_code, child2_code

    def mutate(self, genetic_code):
        if random.uniform(0, 1) < self.mutation_rate:
            random_index = random.randrange(len(genetic_code))
            genetic_code[random_index] = random.uniform(-1, 1)
        return genetic_code

    
    def optimize(self):
        population = self.initial_population()

        global_best = min(population, key = lambda x: x.fitness)
        global_best_iteration_found = 0

        for i in range(self.max_iterations):
            selected = self.selection(population)
            population = self.create_generation(selected)
            current_best = min(population, key = lambda x: x.fitness)
            print(current_best)

            if current_best.fitness < global_best.fitness:
                global_best = current_best
                global_best_iteration_found = i 

            if i - global_best_iteration_found >= 10:
                print("No better chromosome in 10 iterations")
                result = global_best
                break

        return result


def main():
    genetic_algorithm = GeneticAlgorithm()
    result = genetic_algorithm.optimize()
    print("Best found: ", result)


if __name__ == "__main__":
    main()
