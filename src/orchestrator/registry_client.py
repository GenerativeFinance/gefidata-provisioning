"""Interface to on-chain contract for metadata/commits."""
from web3 import Web3
from ..contracts.contract_interface import IncentiveRegistry

class RegistryClient:
    def __init__(self, rpc_url: str, contract_address: str = None):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = IncentiveRegistry(self.w3, contract_address)

    def get_registered_nodes(self) -> list[str]:
        """Fetch list of registered node IDs."""
        return self.contract.get_nodes.call()

    def verify_contribution(self, node_id: str, proof: bytes) -> bool:
        """Verify on-chain proof."""
        return self.contract.verify_proof(node_id, proof).call()