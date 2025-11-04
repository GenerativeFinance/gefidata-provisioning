"""KPIs (convergence, participation, privacy budget)."""
from typing import Dict
import torch

def track_convergence(losses: list[float]) -> Dict:
    """Track loss over rounds."""
    return {"avg_loss": sum(losses)/len(losses), "convergence_rate": (losses[0] - losses[-1]) / losses[0]}

def privacy_budget(epsilons: list[float], deltas: list[float]) -> float:
    """Cumulative epsilon."""
    return sum(epsilons)