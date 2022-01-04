import os
import click


def initial_idea(x, y, w1, w2):
    return max(1, min(5, x + (y - 0.5) * w1) - (1 - y) / w2 * x)


def compute_contrip(x, y, w1, w2):
    return min(5, x + (y - 0.5) * w1) - (1 - y) / w2 * x - (5 - x) / 100


def compute_contrip_now2(x, y, w1):
    return min(5, x + (y - 0.5) * w1) - (1 - y) / (6 - x)


def scaling(score):
    return (score - 0.61) / (5 - 0.61) * 4 + 1



# ------------------------------------------------------------------------------
# CLICK
# ------------------------------------------------------------------------------

@click.command(short_help='script to compute the score of a tripadvisor rating')
@click.option(
    '-tr', '--tripadvisor_rating', default=5.0, 
    help='rating of tripadvisor hotel'
)
@click.option(
    '-cv', '--consensus_value', default=1.0, 
    help='value of consensus analysis through NLP'
)
@click.option(
    '-w1', '--weight_1', default=0.5, 
    help='weight for the importance of the consensus value'
)
@click.option(
    '-w2', '--weight_2', default=10.0, 
    help='weight for the importance of the consensus value 2'
)
@click.option(
    '-o', '--output', default='', help='output folder'
)
def main(tripadvisor_rating, consensus_value, weight_1, weight_2, output):

    assert tripadvisor_rating >= 1 
    
    score = compute_contrip(tripadvisor_rating, consensus_value, weight_1, weight_2)
    print(score)

    new_score = scaling(score)
    print(new_score)



if __name__ == '__main__':
    main()