"""Connectors to local data sources (e.g., DBs, APIs)."""
import sqlalchemy as sa
from typing import Any

class DataConnector:
    def __init__(self, source_type: str, connection_str: str):
        self.engine = sa.create_engine(connection_str)
        self.source_type = source_type

    def load_data(self, table: str) -> Any:
        """Load data from source."""
        if self.source_type == "sql":
            return pd.read_sql(f"SELECT * FROM {table}", self.engine)
        # Add API connector, etc.
        raise NotImplementedError("Connector not implemented")