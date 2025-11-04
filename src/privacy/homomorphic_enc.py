"""HE (if needed)."""
from phe import paillier  # Hypothetical lib

class HEAggregator:
    def __init__(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair()

    def encrypt(self, value: int) -> paillier.EncryptedNumber:
        return paillier.encrypt(self.public_key, value)

    def homomorphic_add(self, enc1: paillier.EncryptedNumber, enc2: paillier.EncryptedNumber) -> paillier.EncryptedNumber:
        return enc1 + enc2

    def decrypt(self, enc: paillier.EncryptedNumber) -> int:
        return paillier.decrypt(self.private_key, enc)