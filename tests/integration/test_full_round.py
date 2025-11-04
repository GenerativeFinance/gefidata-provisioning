"""End-to-end federated round simulation."""
import pytest
from src.orchestrator.round_manager import RoundManager
from src.orchestrator.coordinator import Coordinator

def test_full_round():
    config = "configs/dev_config.yaml"
    coord = Coordinator(config)
    manager = RoundManager(coord)
    participants = coord.select_participants(1)
    manager.start_round(1, participants)
    updates = manager.compute_phase()  # Mock
    verified = manager.aggregate_and_verify(updates)
    assert verified  # Assuming mock passes