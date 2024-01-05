import random



def generate_random_state():

    state = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            state[i][j] = random.randint(0, 2)
    return state



def evaluate_state(state):

    for row in state:
        if row[0] == row[1] == row[2] != 0:
            return 1 if row[0] == 1 else -1


    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col] != 0:
            return 1 if state[0][col] == 1 else -1


    if state[0][0] == state[1][1] == state[2][2] != 0:
        return 1 if state[0][0] == 1 else -1
    if state[0][2] == state[1][1] == state[2][0] != 0:
        return 1 if state[0][2] == 1 else -1

    return 0



def generate_next_generation(current_generation):
    next_generation = []
    population_size = len(current_generation)

    parents = random.choices(current_generation, k=population_size)
    for parent in parents:

        child = [[0, 0, 0] for _ in range(3)]
        for i in range(3):
            for j in range(3):

                if random.random() < 0.3:
                    child[i][j] = random.randint(0, 2)
                else:
                    child[i][j] = parent[i][j]
        next_generation.append(child)
    return next_generation



def evolutionary_algorithm():

    max_generations = 100
    population_size = 50
    termination_condition = False


    current_generation = [generate_random_state() for _ in range(population_size)]

    for generation in range(max_generations):

        evaluated_generation = [(state, evaluate_state(state)) for state in current_generation]


        best_state, best_score = max(evaluated_generation, key=lambda x: x[1])
        if best_score == 1 or best_score == -1:
            termination_condition = True
            break


        current_generation = generate_next_generation([state for state, _ in evaluated_generation])

    
    return best_state



best_solution = evolutionary_algorithm()
print("Best solution:")
for row in best_solution:
    print(row)