"""Small-scale rollout with TEEs."""
import torch
from src.node_agent.trainer import Trainer
from src.node_agent.attestation import Attestor
from src.orchestrator.registry_client import RegistryClient

# Mock consortium: 3 nodes
nodes = ["node1", "node2", "node3"]
attestor = Attestor("nitro")
registry = RegistryClient("http://localhost:8545")

for node in nodes:
    model = torch.nn.Linear(10, 1)
    trainer = Trainer(model, None)
    update = trainer.train_local({"local_epochs": 5})
    data_hash = b"data_hash"
    quote = attestor.generate_attestation(data_hash)
    # Submit to registry
    registry.verify_contribution(node, quote)

print("Consortium pilot complete with TEE attestations.")