"""e.g., FedPer for local heads."""
import torch
from .fedavg import FedAvg

class PersonalizedFL(FedAvg):
    def personalize(self, global_model: torch.nn.Module, local_data: torch.utils.data.DataLoader) -> torch.nn.Module:
        """Fine-tune head on local data."""
        # Freeze base, train head
        for param in global_model.base.parameters():
            param.requires_grad = False
        optimizer = torch.optim.SGD(global_model.head.parameters(), lr=0.01)
        for batch in local_data:
            loss = global_model(batch)
            loss.backward()
            optimizer.step()
        return global_model