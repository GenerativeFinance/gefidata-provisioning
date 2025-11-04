#!/bin/bash
set -e

# Install deps
pip install -e .

# Compile contracts
solc --abi --bin src/contracts/incentive_registry.sol -o build/

# Start local blockchain (Ganache)
ganache-cli --port 8545 --accounts 10 --defaultBalanceEther 100 &

echo "Environment setup complete. Ganache running on 8545."