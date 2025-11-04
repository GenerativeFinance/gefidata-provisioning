"""Cryptographic aggregation."""
from cryptography.fernet import Fernet
from typing import Dict, List

class BonawitzAggregator:
    def __init__(self, num_participants: int):
        self.num_participants = num_participants
        self.keys = [Fernet.generate_key() for _ in range(num_participants)]

    def generate_masks(self, public_keys: List[bytes]) -> Dict:
        """Pairwise masks for Bonawitz."""
        masks = {}
        for i in range(self.num_participants):
            for j in range(i+1, self.num_participants):
                mask = bytes(a ^ b for a, b in zip(self.keys[i], self.keys[j]))
                masks[(i,j)] = mask
        return masks

    def sum_shares(self, shares: Dict[str, bytes]) -> bytes:
        """XOR sum of masked shares."""
        total = b'\x00' * len(next(iter(shares.values())))
        for share in shares.values():
            total = bytes(a ^ b for a, b in zip(total, share))
        return total