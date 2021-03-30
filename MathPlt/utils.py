import matplotlib.pyplot as plt


def save(name='', fmt='png'):
    plt.savefig(f'MathPlt/img/{name}.{fmt}')


def get_discr(a, b, c):
    return b**2-4*a*c