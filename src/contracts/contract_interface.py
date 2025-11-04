"""Python wrapper (using web3.py) for interactions."""
from web3 import Web3
from typing import Optional

# ABI placeholder; in prod, load from compiled JSON
ABI = []  # Load from artifacts

class IncentiveRegistry:
    def __init__(self, w3: Web3, address: Optional[str] = None):
        self.w3 = w3
        self.address = address or "0x..."  # Default dev address
        self.contract = w3.eth.contract(address=self.address, abi=ABI)

    def register_node(self, metadata_uri: str, account: str, private_key: str):
        """Register node."""
        txn = self.contract.functions.registerNode(metadata_uri).build_transaction({
            'from': account, 'gas': 200000, 'gasPrice': self.w3.to_wei('20', 'gwei')
        })
        signed = self.w3.eth.account.sign_transaction(txn, private_key)
        return self.w3.eth.send_raw_transaction(signed.rawTransaction)

    def verify_proof(self, node_id: str, proof: bytes):
        """Call verifyProof."""
        return self.contract.functions.verifyProof(node_id, proof)

    def get_nodes(self):
        """Call getNodes."""
        return self.contract.functions.getNodes()