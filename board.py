import random

class Board:
    def __init__(self, size=8):
        self.size = size
        # موقعیت هر وزیر: اندیس = سطر، مقدار = ستون
        self.queens = [random.randint(0, size - 1) for _ in range(size)]

    def fitness(self):
        """
        تعداد برخوردهای غیرمجاز بین وزیرها را محاسبه می‌کند و سپس آن را از حداکثر حالت‌های ممکن کم می‌کند.
        هدف: هر چه fitness بیشتر، حالت بهتر.
        """
        conflicts = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                # در یک ستون یا قطر مشترک
                if self.queens[i] == self.queens[j] or \
                   abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        max_fitness = (self.size * (self.size - 1)) // 2  # بدون برخورد
        return max_fitness - conflicts

    def __str__(self):
        return f"Queens: {self.queens} | Fitness: {self.fitness()}"
