"""Online delta-performance attribution."""
import torch
from typing import Dict

class ContributionScorer:
    def score_delta(self, old_model: torch.nn.Module, new_model: torch.nn.Module, test_loss: float) -> float:
        """Score based on performance delta."""
        old_loss = self.evaluate(old_model)  # Placeholder eval
        delta = old_loss - test_loss
        return delta / (1 + abs(delta))  # Normalized [-1,1]

    def evaluate(self, model: torch.nn.Module) -> float:
        # Dummy eval
        return 0.5