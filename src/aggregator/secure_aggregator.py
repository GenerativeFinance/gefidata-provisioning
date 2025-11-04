"""Implements Bonawitz protocol or MPC."""
from ..privacy.secure_aggregation import BonawitzAggregator
from typing import Dict, List

class SecureAggregator:
    def __init__(self, num_participants: int):
        self.agg = BonawitzAggregator(num_participants)

    def setup_keys(self, public_keys: List[bytes]) -> Dict:
        """Generate pairwise masks."""
        return self.agg.generate_masks(public_keys)

    def aggregate_encrypted(self, shares: Dict[str, bytes]) -> bytes:
        """Secure sum."""
        return self.agg.sum_shares(shares)