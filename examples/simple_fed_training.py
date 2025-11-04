"""Basic FedAvg round with mock data."""
import torch
from flwr import ServerApp
from src.orchestrator.round_manager import RoundManager
from src.orchestrator.coordinator import Coordinator

# Mock setup
config = "configs/default_config.yaml"
coord = Coordinator(config)
manager = RoundManager(coord)

# Simulate 3 rounds
for round_id in range(1, 4):
    participants = coord.select_participants(2)
    manager.start_round(round_id, participants)
    # Mock compute
    updates = {"updates": [torch.rand(10, 10) for _ in participants], "proofs": {p: b"proof" for p in participants}}
    verified = manager.aggregate_and_verify(updates)
    print(f"Round {round_id} verified: {verified}")

print("Simple FedAvg simulation complete.")