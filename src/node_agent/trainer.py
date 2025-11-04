"""Local training with constraints (e.g., DP-SGD)."""
import torch
from opacus import PrivacyEngine
from ..privacy.differential_privacy import apply_dp_sgd
from ..algorithms.fedavg import FedAvgClient

class Trainer:
    def __init__(self, model: torch.nn.Module, data_loader: torch.utils.data.DataLoader):
        self.model = model
        self.data_loader = data_loader
        self.client = FedAvgClient()

    def train_local(self, config: dict) -> dict:
        """Run local epochs with DP."""
        optimizer = torch.optim.SGD(self.model.parameters(), lr=config["lr"])
        privacy_engine = PrivacyEngine()
        self.model, optimizer, self.data_loader = privacy_engine.make_private(
            module=self.model, optimizer=optimizer, data_loader=self.data_loader,
            noise_multiplier=config["noise_multiplier"], max_grad_norm=config["max_grad_norm"]
        )
        for epoch in range(config["local_epochs"]):
            for batch in self.data_loader:
                loss = self.model(batch[0], batch[1])
                loss.backward()
                optimizer.step()
        delta_params = self.client.get_parameters(self.model)
        return {"delta": delta_params}