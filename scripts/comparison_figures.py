import os
import click
import numpy as np
import pandas as pd

def compute_contrip(x, y, w1, w2):
    return np.minimum(np.full((200, 5), 5), x + (y - 0.5) * w1) - (1 - y) / w2 * x


# ------------------------------------------------------------------------------
# CLICK
# ------------------------------------------------------------------------------

@click.command(short_help='script to study how different parameters change' 
    'the behavior of the score of a tripadvisor rating')
@click.option(
    '-w1', '--weight_1', default=1.2, 
    help='weight for the importance of the consensus value'
)
@click.option(
    '-w2', '--weight_2', default=10.0, 
    help='weight for the importance of the consensus value 2'
)
@click.option(
    '-o', '--output', default='', help='output folder'
)
def main(weight_1, weight_2, output):
    
    rating = np.linspace(1, 5, 5).reshape(1, 5)
    consensus = np.linspace(0, 1, 200).reshape(200, 1)

    score = compute_contrip(rating, consensus, weight_1, weight_2)

    import pdb;pdb.set_trace()

    df = pd.DataFrame(score)
    print(score)



if __name__ == '__main__':
    main()