"""DP-SGD, DP-FedAvg."""
import torch
from opacus import PrivacyEngine

def apply_dp_sgd(model: torch.nn.Module, optimizer: torch.optim.Optimizer, data_loader: torch.utils.data.DataLoader,
                 noise_multiplier: float, max_grad_norm: float):
    """Apply DP to training loop."""
    privacy_engine = PrivacyEngine()
    model, optimizer, data_loader = privacy_engine.make_private(
        module=model,
        optimizer=optimizer,
        data_loader=data_loader,
        noise_multiplier=noise_multiplier,
        max_grad_norm=max_grad_norm,
    )
    return model, optimizer, data_loader