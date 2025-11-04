"""Metadata queries (who has features), local serving schema."""
import yaml
from typing import Dict, List

class FFS:
    def __init__(self, metadata_file: str = "features.yaml"):
        with open(metadata_file, 'r') as f:
            self.metadata = yaml.safe_load(f)

    def query_features(self, feature_type: str) -> List[Dict]:
        """Query who has which features."""
        return [node for node in self.metadata["nodes"] if feature_type in node["features"]]

    def serve_schema(self, feature_id: str) -> Dict:
        """Local schema for serving."""
        return self.metadata["schemas"].get(feature_id, {})