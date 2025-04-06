"""from board import Board

if __name__ == "__main__":
    b = Board()
    print(b)"""

"""from algorithm import generate_population, selection

if __name__ == "__main__":
    population = generate_population(10)
    for i, individual in enumerate(population):
        print(f"{i+1}: {individual}")

    parent1, parent2 = selection(population)
    print("\nSelected Parents:")
    print("Parent 1:", parent1)
    print("Parent 2:", parent2)
"""
"""from algorithm import generate_population, selection, crossover, mutate

if __name__ == "__main__":
    population = generate_population(10)
    parent1, parent2 = selection(population)

    print("Parent 1:", parent1)
    print("Parent 2:", parent2)

    child = crossover(parent1, parent2)
    print("\nChild before mutation:", child)

    mutate(child, mutation_rate=0.3)
    print("Child after mutation:", child)
"""
from algorithm import genetic_algorithm

if __name__ == "__main__":
    solution = genetic_algorithm(pop_size=20, board_size=8, max_generations=1000, mutation_rate=0.2)
    print("\nFinal Board:")
    print(solution)
