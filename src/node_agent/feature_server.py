"""API for federated feature provisioning (on-demand or pre-computed)."""
from flask import Flask, request, jsonify
from ..feature_store.ffs import FFS

app = Flask(__name__)
ffs = FFS()

@app.route('/features/<feature_id>', methods=['GET'])
def serve_feature(feature_id: str):
    """Serve features based on metadata query."""
    query = request.args.get('query', '')
    features = ffs.query_and_serve(feature_id, query)
    return jsonify({"features": features})

def run_server(port: int = 5000):
    app.run(port=port)