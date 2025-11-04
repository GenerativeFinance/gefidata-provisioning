"""Approximate Shapley/Influence functions."""
import numpy as np
from itertools import combinations
from typing import List, Callable

class ShapleyEstimator:
    def __init__(self, utility_fn: Callable, players: List[str]):
        self.utility = utility_fn
        self.players = players

    def approximate_shapley(self, n_samples: int = 100) -> Dict[str, float]:
        """Monte Carlo approximation."""
        values = {}
        for player in self.players:
            total = 0.0
            for _ in range(n_samples):
                # Random permutation
                perm = np.random.permutation(self.players)
                idx = np.where(perm == player)[0][0]
                s1 = set(perm[:idx])
                s2 = set(perm[idx+1:])
                v1 = self.utility(s1 | {player}) - self.utility(s1)
                total += v1 * np.math.factorial(len(self.players) - 1) / np.math.factorial(len(s1))
            values[player] = total / n_samples
        return values