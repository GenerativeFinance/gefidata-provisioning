# Round Lifecycle Pseudocode

# ORCHESTRATOR (Global Coordinator)

for round in range(1, MAX_ROUNDS + 1):

    # 1. Select eligible participants based on reputation threshold
    participants = select_nodes(reputation > THRESHOLD)

    # 2. Send the current global model to participants
    broadcast_init(global_model)

    # 3. Collect masked updates + ZK proofs from nodes
    masked_updates = []
    proofs = []

    for node in participants:
        update = node.train_local(global_model, local_data, config)
        proof = zk_prove(update, private_data)
        masked_update = secure_mask(update, keys)

        submit(masked_update, proof)

        masked_updates.append(masked_update)
        proofs.append(proof)

    # 4. Aggregate updates and verify validity
    global_update = aggregate(masked_updates)
    verify_proofs(proofs)

    # 5. Compute contribution scores (e.g. Shapley Value)
    scores = score_contributions(masked_updates)

    # 6. Distribute on-chain rewards ba
