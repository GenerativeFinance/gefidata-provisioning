"""Round initialization, participant selection, proof verification."""
import random
from typing import List, Dict
from ..utils.config_parser import load_config
from .registry_client import RegistryClient

class Coordinator:
    def __init__(self, config_path: str):
        self.config = load_config(config_path)
        self.registry = RegistryClient(self.config["blockchain"]["rpc_url"])

    def select_participants(self, num_rounds: int) -> List[str]:
        """Select participants based on reputation and availability."""
        all_nodes = self.registry.get_registered_nodes()
        # Simple random selection for demo; replace with weighted sampling
        return random.sample(all_nodes, min(num_rounds, len(all_nodes)))

    def verify_proofs(self, proofs: Dict[str, bytes]) -> bool:
        """Verify ZK proofs from participants."""
        for node_id, proof in proofs.items():
            if not self.registry.verify_contribution(node_id, proof):
                return False
        return True