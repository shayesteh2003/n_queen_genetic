from board import Board
import random

def generate_population(pop_size=10, board_size=8):
    """
    تولید جمعیتی از حالت‌های تصادفی
    """
    return [Board(size=board_size) for _ in range(pop_size)]

def selection(population):
    """
    انتخاب دو فرد با بیشترین Fitness
    """
    sorted_population = sorted(population, key=lambda b: b.fitness(), reverse=True)
    return sorted_population[0], sorted_population[1]  # والدین برتر

def crossover(parent1, parent2):
    """
    ترکیب دو والد برای تولید فرزند
    از روش تک نقطه‌ای (single-point crossover)
    """
    size = parent1.size
    crossover_point = random.randint(1, size - 2)
    
    child_queens = parent1.queens[:crossover_point] + parent2.queens[crossover_point:]
    
    child = Board(size=size)
    child.queens = child_queens
    return child

def mutate(individual, mutation_rate=0.1):
    """
    تغییر تصادفی در موقعیت یک وزیر
    """
    for i in range(individual.size):
        if random.random() < mutation_rate:
            individual.queens[i] = random.randint(0, individual.size - 1)


def genetic_algorithm(pop_size=10, board_size=8, max_generations=1000, mutation_rate=0.1):
    population = generate_population(pop_size, board_size)
    max_fitness = (board_size * (board_size - 1)) // 2  # بیشترین امتیاز ممکن (یعنی بدون کانفلیکت)

    for generation in range(max_generations):
        # بررسی برای جواب
        best = max(population, key=lambda b: b.fitness())
        if best.fitness() == max_fitness:
            print(f"\n✅ Solution found in generation {generation}:")
            return best

        # انتخاب والدین
        parent1, parent2 = selection(population)

        # تولید فرزند جدید
        child = crossover(parent1, parent2)
        mutate(child, mutation_rate)

        # جایگزینی: جایگزینی ضعیف‌ترین عضو با فرزند جدید
        population.sort(key=lambda b: b.fitness())
        population[0] = child

    # در صورت عدم پیدا شدن راه‌حل کامل
    print("\n❌ No perfect solution found.")
    return max(population, key=lambda b: b.fitness())
