"""Unit tests for algorithms."""
import pytest
import torch
from src.algorithms.fedavg import FedAvg

def test_fedavg_aggregate():
    updates = [{"params": {"w": torch.tensor([1.0])}, "num_samples": 10},
               {"params": {"w": torch.tensor([3.0])}, "num_samples": 20}]
    avg = FedAvg.aggregate(updates)
    assert avg["w"] == pytest.approx(torch.tensor(2.6667))