"""Encryption, hashing, Merkle roots."""
import hashlib
from typing import List

def compute_hash(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def compute_merkle_root(leaves: List[bytes]) -> bytes:
    if not leaves:
        return b""
    if len(leaves) == 1:
        return leaves[0]
    # Recursive pairing
    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1])
    parents = [compute_hash(a + b) for a, b in zip(leaves[::2], leaves[1::2])]
    return compute_merkle_root(parents)