from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
DECIMAL = 8
STARTING_PRICE =20000000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev2"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network id {network.show_active()}")
    print("Deploying Mock ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
        print("Mocks deployed")