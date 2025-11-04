"""Lifecycle management (init, compute, aggregate, verify)."""
from enum import Enum
from typing import Any
from ..algorithms.fedavg import FedAvg
from .coordinator import Coordinator

class RoundState(Enum):
    INIT = "init"
    COMPUTE = "compute"
    AGGREGATE = "aggregate"
    VERIFY = "verify"

class RoundManager:
    def __init__(self, coordinator: Coordinator):
        self.coordinator = coordinator
        self.state = RoundState.INIT
        self.algorithm = FedAvg()  # Default; configurable

    def start_round(self, round_id: int, participants: list[str]) -> None:
        """Initialize round."""
        self.state = RoundState.INIT
        # Broadcast init signal
        print(f"Starting round {round_id} with {len(participants)} participants")

    def compute_phase(self) -> Any:
        """Wait for local computes."""
        self.state = RoundState.COMPUTE
        # Simulate wait; in prod, use Flower server
        return {"updates": []}  # Placeholder

    def aggregate_and_verify(self, updates: dict) -> bool:
        """Aggregate and verify."""
        self.state = RoundState.AGGREGATE
        global_model = self.algorithm.aggregate(updates)
        self.state = RoundState.VERIFY
        return self.coordinator.verify_proofs(updates["proofs"])