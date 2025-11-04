#!/bin/bash
set -e

# Run full round simulation
python examples/simple_fed_training.py

# Run consortium pilot
python examples/consortium_pilot.py

echo "Simulation complete."