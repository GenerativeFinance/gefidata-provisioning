"""Proof-of-aggregation, anomaly detection."""
import numpy as np
from scipy import stats

class Verifier:
    @staticmethod
    def check_aggregation_proof(agg_root: bytes, expected_root: bytes) -> bool:
        """Verify Merkle root of aggregation."""
        return agg_root == expected_root

    @staticmethod
    def detect_anomalies(updates: list[np.ndarray], threshold: float = 3.0) -> list[int]:
        """Z-score based anomaly detection."""
        z_scores = np.abs(stats.zscore(updates))
        return [i for i, z in enumerate(z_scores) if z > threshold]