"""Unit tests for node agent."""
import pytest
import torch
from src.node_agent.trainer import Trainer

@pytest.fixture
def dummy_model():
    return torch.nn.Linear(10, 1)

def test_local_train(dummy_model):
    trainer = Trainer(dummy_model, None)  # Mock data_loader
    update = trainer.train_local({"local_epochs": 1, "lr": 0.01, "noise_multiplier": 1.0, "max_grad_norm": 1.0})
    assert "delta" in update