// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IncentiveRegistry {
    struct Node {
        address owner;
        string metadataURI;
        uint256 reputation;
    }

    mapping(address => Node) public nodes;
    mapping(uint256 => bytes32) public roundCommits;
    uint256 public roundCounter;

    event NodeRegistered(address indexed node, string metadataURI);
    event ContributionVerified(uint256 indexed round, address indexed node, bool valid);

    modifier onlyRegistered(address node) {
        require(nodes[node].owner != address(0), "Node not registered");
        _;
    }

    function registerNode(string memory _metadataURI) public {
        nodes[msg.sender] = Node(msg.sender, _metadataURI, 0);
        emit NodeRegistered(msg.sender, _metadataURI);
    }

    function submitCommit(uint256 roundId, bytes32 commit) public onlyRegistered(msg.sender) {
        require(roundId == roundCounter, "Invalid round");
        roundCommits[roundId] = commit;
    }

    function verifyProof(address node, bytes memory proof) public onlyRegistered(node) returns (bool) {
        // Placeholder verification logic
        bool valid = keccak256(proof) == roundCommits[roundCounter];
        if (valid) {
            nodes[node].reputation += 1;
        }
        emit ContributionVerified(roundCounter, node, valid);
        return valid;
    }

    function getNodes() public view returns (address[] memory) {
        // Implementation for listing nodes (use array or events for prod)
        address[] memory nodeList = new address[](0);
        return nodeList;
    }
}