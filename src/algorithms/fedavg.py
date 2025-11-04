"""Baseline weighted average."""
import torch
from flwr.common import ndarrays_to_parameters
from typing import Dict, List

class FedAvg:
    @staticmethod
    def aggregate(client_updates: List[Dict]) -> torch.nn.Module:
        """Weighted average of model params."""
        num_samples = sum(update["num_samples"] for update in client_updates)
        avg_params = {name: torch.zeros_like(param) for name, param in client_updates[0]["params"].items()}
        total_weight = 0.0
        for update in client_updates:
            weight = update["num_samples"] / num_samples
            for name, param in update["params"].items():
                avg_params[name] += weight * param
            total_weight += weight
        # Update global model (placeholder)
        return avg_params  # Return as dict

class FedAvgClient:
    def get_parameters(self, model: torch.nn.Module) -> Dict[str, torch.Tensor]:
        """Extract params."""
        return {name: param.clone() for name, param in model.named_parameters()}