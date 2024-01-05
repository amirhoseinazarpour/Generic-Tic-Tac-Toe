import random

# تعریف جمعیت اولیه
def create_population(population_size):
    population = []
    for _ in range(population_size):
        individual = []
        for _ in range(9):  # 9 خانه در بازی دوز
            individual.append(random.choice([0, 1, 2]))  # 0: خانه خالی، 1: نقش اولیه، 2: نقش دوم
        population.append(individual)
    return population

# ارزیابی هر فرد در جمعیت
def evaluate_population(population):
    scores = []
    for individual in population:
        score = evaluate_individual(individual)
        scores.append(score)
    return scores

# ارزیابی یک فرد خاص
def evaluate_individual(individual):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # یک صفحه خالی 3x3 برای بازی دوز
    num_ones = individual.count(1)  # تعداد 1 ها در حالت فرد
    num_twos = individual.count(2)  # تعداد 2 ها در حالت فرد

    if abs(num_ones - num_twos) > 1:
        return 0  # تعداد 1 ها و 2 ها بیش از حد مجاز است

    # تبدیل حالت فرد به صفحه بازی
    for i in range(9):
        row = i // 3
        col = i % 3
        if individual[i] == 1:
            board[row][col] = 1  # نقش اولیه
        elif individual[i] == 2:
            board[row][col] = 2  # نقش دوم

    # بررسی برنده بودن
    winning_positions = [
        [[0, 0], [0, 1], [0, 2]],  # سطرهای افقی
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],  # ستون‌های عمودی
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],  # قطرها
        [[0, 2], [1, 1], [2, 0]]
    ]

    score = 0
    for positions in winning_positions:
        values = [board[row][col] for row, col in positions]
        if values == [1, 1, 1]:
            score += 1  # امتیاز برای بازیکن 1 (نقش اولیه)
        elif values == [2, 2, 2]:
            score += 1  # امتیاز برای بازیکن 2 (نقش دوم)

    return score
# انتخاب والدین برای تولید نسل جدید
def select_parents(population, scores, num_parents):
    parents = []
    for _ in range(num_parents):
        max_score_index = scores.index(max(scores))
        parents.append(population[max_score_index])
        scores[max_score_index] = -1  # برای جلوگیری از انتخاب دوباره والدین با بیشترین امتیاز
    return parents

# تولید نسل جدید با استفاده از عملیات ژنتیک
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

# جهش در گروه جدید
def mutate(offspring):
    mutated_offspring = []
    for child in offspring:
        mutated_child = child
        for i in range(9):
            if random.random() < 0.1:  # احتمال جهش
                mutated_child[i] = random.choice([0, 1, 2])
        mutated_offspring.append(mutated_child)
    return mutated_offspring

# الگوریتم ژنتیک
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

# استفاده از الگوریتم ژنتیک برای حل بازی دوز
best_solution = genetic_algorithm(population_size=100, num_generations=50)
print("Best solution:", best_solution)