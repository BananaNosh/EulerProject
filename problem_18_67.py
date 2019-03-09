from tools import read_input_line_wise
import nia.Week_2.AbstractModules as AM
from nia.Week_2.GeneticAlgorithm import GeneticAlgorithm
from nia.Week_2.Initializer import ZeroInitializer
from nia.Week_2.Mutator import BitFlipMutator
from nia.Week_2.Recombiner import KPointCrossover
from nia.Week_2.Replacer import SteadyStateReplacer
from nia.Week_2.Selector import RouletteSelector
import matplotlib.pyplot as plt


# problem 18
class MaxPathSumProblem(AM.AbstractProblem):
    def __init__(self, numbers):
        self.numbers = numbers

    def chromosome_size(self):
        return len(self.numbers) - 1

    def allele_count(self):
        return 2

    def create_individual(self, chromosome, fitness=None):
        return Individual(self, chromosome, fitness)


class Individual(AM.AbstractIndividual):
    def _calculate_fitness(self):
        numbers = self.problem.numbers
        fitness = numbers[0][0]  # allways with first number
        index = 0
        for number_line, allele in zip(numbers[1:], self.chromosome):
            if allele:
                index += 1
            fitness += number_line[index]
        return fitness


def genetic_algorithm(lines):
    numbers = [[int(number) for number in line.strip().split()] for line in lines]
    problem = MaxPathSumProblem(numbers)
    population_size = 100
    selection_size = population_size
    recombination_parent_count = 2
    crossover_probability = 0.6
    crossover_point_count = 1
    mutation_probability = 0.1
    initializer = ZeroInitializer(problem, population_size)
    selector = RouletteSelector(selection_size)
    recombiner = KPointCrossover(recombination_parent_count, crossover_probability, crossover_point_count)
    mutator = BitFlipMutator(mutation_probability, problem.allele_count())
    replacer = SteadyStateReplacer(population_size // 2)
    algorithm = GeneticAlgorithm(initializer, selector, recombiner, mutator, replacer)
    algorithm.run(10)
    algorithm.plot_result()
    plt.show()


def brute_force(lines):
    numbers = [[int(number) for number in line.strip().split()] for line in lines]
    problem = MaxPathSumProblem(numbers)
    greatest = 0
    for i in range(2**len(numbers)):
        chromosome = [int(b) for b in bin(i)[2:]]
        fitness = Individual(problem, chromosome).fitness
        if fitness > greatest:
            greatest = fitness
        print(chromosome, fitness)
    print(greatest)


def clever_depth_search(lines):
    numbers = [[int(number) for number in line.strip().split()] for line in lines]
    max_rest = [max(numbers[-1])]
    for i, line in enumerate(reversed(numbers[:-1])):
        max_rest.append(max(line) + max_rest[i])
    max_rest = list(reversed(max_rest))
    best_found = 0
    line_count = len(numbers)
    for i in range(2 ** line_count):
        if i % 100000 == 0:
            print(i, best_found)
        index = 0
        fitness = numbers[0][0]
        for j, number_line in enumerate(numbers[1:]):
            upper_bound = fitness + max_rest[j+1]
            if upper_bound <= best_found:
                break
            direction = i % 2
            i //= 2
            if direction:
                index += 1
            fitness += number_line[index]
        if fitness > best_found:
            best_found = fitness
    return best_found


if __name__ == '__main__':
    lines = read_input_line_wise(67)
    # genetic_algorithm(lines)
    # brute_force(lines)
    print(clever_depth_search(lines))
