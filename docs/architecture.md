# Architecture

## High-Level Goals
- Privacy: No raw data leaves nodes.
- Incentives: Blockchain rewards for contributions.
- Compliance: ZK proofs for audits.
- Scalability: Kubernetes deployment.

## Components
- **Orchestrator**: Central coordinator (Flower server + custom).
- **Node Agent**: Local FL client + feature API.
- **Aggregator**: Secure sum via MPC/HE.
- **Feature Store**: Metadata-only federation.
- **Contracts**: Solidity for registry/rewards.
- **Compliance**: Policy checks + notifier.

## Data Flows
1. Orchestrator selects nodes via on-chain registry.
2. Nodes train locally (DP-SGD), attest in TEE, submit masked updates + ZK proofs.
3. Aggregator sums masks, verifies proofs.
4. Global model broadcast; contributions scored (Shapley) for rewards.

See `pseudocode.md` for details.