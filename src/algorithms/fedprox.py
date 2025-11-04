"""For non-IID data."""
import torch
from .fedavg import FedAvg

class FedProx(FedAvg):
    def __init__(self, mu: float = 0.01):
        self.mu = mu  # Proximity parameter

    def local_update(self, model: torch.nn.Module, global_params: Dict, data_loader: torch.utils.data.DataLoader) -> Dict:
        """Proximal term in loss."""
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        for epoch in range(5):  # Local epochs
            for batch in data_loader:
                loss = self.compute_loss(model, batch)
                prox_term = sum((p - g)**2 for p, g in zip(model.parameters(), global_params.values())) * self.mu / 2
                total_loss = loss + prox_term
                total_loss.backward()
                optimizer.step()
        return self.get_parameters(model)