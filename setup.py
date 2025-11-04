from setuptools import setup, find_packages

setup(
    name="gefidata-provisioning",
    version="0.1.0",
    author="GEFI Contributors",
    description="Privacy-preserving federated learning with incentivized features",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flower==1.8.0",
        "torch==2.1.0",
        "opacus==1.4.0",
        "web3==6.11.0",
        "cryptography==41.0.0",
        "numpy==1.24.0",
        "pandas==2.0.0",
        "pyyaml==6.0",
        "requests==2.31.0",
        "sqlalchemy==2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.0",
            "black==23.0.0",
            "sphinx==7.0.0",
            "sphinx-rtd-theme==1.2.0",
            "flake8==6.0.0",
            "mypy==1.5.0",
        ]
    },
    python_requires=">=3.10",
)