"""For heterogeneous settings."""
import torch
from .fedavg import FedAvg

class SCAFFOLD(FedAvg):
    def __init__(self):
        self.control_variates = {}  # Server and client CVs

    def update_control_variates(self, gradients: Dict, cv: torch.Tensor) -> torch.Tensor:
        """Update CV as gradient estimate."""
        return gradients - cv  # Variance reduction