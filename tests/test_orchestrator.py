"""Unit tests for orchestrator."""
import pytest
from src.orchestrator.coordinator import Coordinator
from src.orchestrator.round_manager import RoundManager

def test_select_participants():
    coord = Coordinator("configs/dev_config.yaml")
    participants = coord.select_participants(5)
    assert len(participants) <= 5

def test_round_lifecycle():
    coord = Coordinator("configs/dev_config.yaml")
    manager = RoundManager(coord)
    manager.start_round(1, ["node1"])
    assert manager.state == RoundManager.RoundState.INIT