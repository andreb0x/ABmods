import requests
import web3
import numpy as np
from web3 import Web3 

WEB3 = Web3(Web3.WebsocketProvider("wss://wsapi.fantom.network/"))


def call_allblocks(contract_fn,delta_blocknums=10**5,current_block=None,vv=False):
    """
    calls contract_fn on all blocks, 
        starting from current block and working back
    contract_fn is a contract read method
    delta_blocknums is the stepsize 
        (checking all blocks takes too long) 
    """
    data = []
    bn = current_block or WEB3.eth.get_block_number() # current block num
    while True:
        if vv: print(bn)
        bn -= delta_blocknums
        try:
            datum = contract_fn.call(block_identifier=bn)
            data.append(datum)
        except:
            break
    data.reverse()
    return data


