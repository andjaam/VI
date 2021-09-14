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
        self.generation_size = 5000
        self.chromosome_size = len(self.target)
        self.tournament_size = 10
        self.reproduction_size = 1000
        self.selection_function = self.roulette_selection
        self.mutation_rate = 0.1

        self.target_fitness = self.calculate_fitness(self.target) - 3

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
    def selection(self, population):
        result = [self.selection_function(population) for _ in range(self.reproduction_size)]
        return result

    def roulette_selection(self, population):
        result = random.choices(population, weights=[x.fitness for x in population], k=1)
        return result[0]

    def tournament_selection(self, population):
        selected = random.sample(population, self.tournament_size)
        result = max(selected, key = lambda x: x.fitness)
        return result


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
            genetic_code[random_index] = random.choice(self.possible_gene_values)
        return genetic_code


    #4
    def best_fit(self, current_best):
        return current_best.fitness >= self.target_fitness
    

    def optimize(self):
        population = self.initial_population()
        
        for _ in range(self.max_iterations):
            selected = self.selection(population)  
            population = self.create_generation(selected)          
            current_best = max(population, key = lambda x: x.fitness)
            print(current_best)
            if self.best_fit(current_best):
                result = current_best
                break
        
        return result


def get_random_string(n):
    return [random.choice(list(string.ascii_letters)) for _ in range(n)]


def main():
    genetic_algorithm = GeneticAlgorithm(string.ascii_letters, get_random_string(10))
    result = genetic_algorithm.optimize()
    print("Best found: ", result)
    

if __name__ == "__main__":
    main()
