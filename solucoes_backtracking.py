"""
Autor: Gabriel Levasseur Rocha Martins
Instituição: PUCRS
Disciplina/Trabalho: Implementação de Backtracking (N-Rainhas e Soma dos Subconjuntos)
"""

import time
import random

class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.iterations = 0
        self.board = [-1] * n

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row=0, find_all=True):
        self.iterations += 1
        if row == self.n:
            self.solutions.append(list(self.board))
            return not find_all

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve(row + 1, find_all):
                    return True
        return False

    def run(self, find_all=True):
        start = time.perf_counter()
        self.solve(0, find_all)
        end = time.perf_counter()
        return len(self.solutions), self.iterations, (end - start) * 1000

class SubsetSum:
    def __init__(self, numbers, target):
        self.numbers = sorted(numbers)
        self.target = target
        self.solutions = []
        self.iterations = 0

    def solve(self, index=0, current_sum=0, path=None, find_all=True):
        if path is None: path = []
        self.iterations += 1

        if current_sum == self.target:
            self.solutions.append(list(path))
            return not find_all

        for i in range(index, len(self.numbers)):
            num = self.numbers[i]
            if current_sum + num > self.target:
                break
            
            path.append(num)
            if self.solve(i + 1, current_sum + num, path, find_all):
                return True
            path.pop()
        return False

    def run(self, find_all=True):
        start = time.perf_counter()
        self.solve(0, 0, [], find_all)
        end = time.perf_counter()
        return len(self.solutions), self.iterations, (end - start) * 1000

def main():
    print(" Executando N-Rainhas...")
    for n in [8, 12]:
        for mode, find_all in [("Primeira", False), ("Todas", True)]:
            nq = NQueens(n)
            sols, iters, t = nq.run(find_all)
            print(f"N={n} | {mode} | Sols: {sols} | Iters: {iters} | Tempo: {t:.2f}ms")

    print("\n Executando Soma dos Subconjuntos...")
    set_15 = [3, 8, 9, 14, 15, 17, 21, 25, 28, 31, 35, 38, 41, 45, 50]
    
    random.seed(42)
    set_25 = [random.randint(1, 100) for _ in range(25)]
    
    test_cases = [(15, set_15, 100), (25, set_25, sum(set_25)//3)]
    
    for size, subset, target in test_cases:
        for mode, find_all in [("Primeira", False), ("Todas", True)]:
            ss = SubsetSum(subset, target)
            sols, iters, t = ss.run(find_all)
            print(f"N={size} | {mode} | Sols: {sols} | Iters: {iters} | Tempo: {t:.2f}ms")

if __name__ == "__main__":
    main()
