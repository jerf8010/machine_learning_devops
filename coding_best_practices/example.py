'''
Module for compute_total_price function

Author: Emanuel
Date: 2024-02-16
'''

import numpy as np


def compute_total_price(path):
    '''
    Takes data from path and return total price

    Args:
        path: (str) Path for file containing gift costs
    Returns:
        total_price: (float) Total price for gift with cost under 25
    '''

    with open(path, encoding='utf-8') as file_path:
        gift_costs = file_path.read().split('\n')
    gift_costs = np.array(gift_costs).astype(int)
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    return total_price


if __name__ == "__main__":
    price = compute_total_price('gift_costs.txt')
    print(price)
