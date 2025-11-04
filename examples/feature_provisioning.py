"""Inference-time feature serving."""
from src.node_agent.feature_server import run_server
from src.feature_store.ffs import FFS

ffs = FFS("configs/features.yaml")  # Assume file
print("Available features:", ffs.query_features("credit_score"))

# Start server
run_server(port=5001)
# Query: curl "http://localhost:5001/features/credit_score?query=age>30"