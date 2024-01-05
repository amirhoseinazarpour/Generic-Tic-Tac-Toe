import random


def create_population(population_size):
    population = []
    for _ in range(population_size):
        individual = []
        for _ in range(9):  
            individual.append(random.choice([0, 1, 2]))  
        population.append(individual)
    return population


def evaluate_population(population):
    scores = []
    for individual in population:
        score = evaluate_individual(individual)
        scores.append(score)
    return scores


def evaluate_individual(individual):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  
    num_ones = individual.count(1)  
    num_twos = individual.count(2)  

    if abs(num_ones - num_twos) > 1:
        return 0  

    
    for i in range(9):
        row = i // 3
        col = i % 3
        if individual[i] == 1:
            board[row][col] = 1  
        elif individual[i] == 2:
            board[row][col] = 2  

   
    winning_positions = [
        [[0, 0], [0, 1], [0, 2]],  
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],  
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]], 
        [[0, 2], [1, 1], [2, 0]]
    ]

    score = 0
    for positions in winning_positions:
        values = [board[row][col] for row, col in positions]
        if values == [1, 1, 1]:
            score += 1  
        elif values == [2, 2, 2]:
            score += 1  

    return score

def select_parents(population, scores, num_parents):
    parents = []
    for _ in range(num_parents):
        max_score_index = scores.index(max(scores))
        parents.append(population[max_score_index])
        scores[max_score_index] = -1  
    return parents


def crossover(parents, offspring_size):
    offspring = []
    while len(offspring) < offspring_size:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = []
        for i in range(9):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        offspring.append(child)
    return offspring


def mutate(offspring):
    mutated_offspring = []
    for child in offspring:
        mutated_child = child
        for i in range(9):
            if random.random() < 0.1:  
                mutated_child[i] = random.choice([0, 1, 2])
        mutated_offspring.append(mutated_child)
    return mutated_offspring


def genetic_algorithm(population_size, num_generations):
    population = create_population(population_size)
    for _ in range(num_generations):
        scores = evaluate_population(population)
        parents = select_parents(population, scores, population_size // 2)
        offspring = crossover(parents, population_size - len(parents))
        mutated_offspring = mutate(offspring)
        population = parents + mutated_offspring
    best_individual_index = scores.index(max(scores))
    best_individual = population[best_individual_index]
    return best_individual


best_solution = genetic_algorithm(population_size=100, num_generations=50)
print("Best solution:", best_solution)
