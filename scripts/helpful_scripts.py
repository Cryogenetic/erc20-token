from brownie import config, accounts, network


LOCAL_BLOCKCHAIN_ENVIRONMENT = [
    "development",
    "ganache-local",
    "hardhat",
    "ganache",
    "mainnet-fork",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print(accounts[0].balance())
        return accounts[0]
    if id:
        return accounts.load(id)
    else:
        return accounts.add(config["wallets"]["from_key"])
