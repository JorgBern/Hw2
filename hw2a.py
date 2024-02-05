# ChatGPT was used to help me write this code
from math import sqrt, pi, exp


def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability based on the provided probability density function (PDF).

    Args:
    - PDF (function): The probability density function.
    - args (tuple): Tuple containing the parameters for the PDF.
    - c (float): Threshold value.
    - GT (bool): If True, calculate P(X > c), else calculate P(X < c).

    Returns:
    float: The calculated probability.
    """
    mu, sig = args
    lhl = mu - 5 * sig
    rhl = c

    if not GT:
        lhl, rhl = rhl, lhl

    args1 = (mu, sig, lhl, rhl)
    p = Simpson(lambda x: PDF(x, args[0], args[1]), args1)
    return p


def GPDF(x, mu, sig):
    """
    Gaussian Probability Density Function (PDF).

    Args:
    - x (float): Input value.
    - mu (float): Mean of the distribution.
    - sig (float): Standard deviation of the distribution.

    Returns:
    float: The probability density at the given point.
    """
    fx = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2)
    return fx


def Simpson(fx, args):
    """
    Perform numerical integration using Simpson's rule.

    Args:
    - fx (function): The function to integrate.
    - args (tuple): Tuple containing integration bounds.

    Returns:
    float: The approximate integral value.
    """
    a, b = args[2], args[3]
    h = (b - a) / 20

    x_values = [a + i * h for i in range(21)]
    fx_values = [fx(x) for x in x_values]

    area = fx_values[0] + fx_values[-1]

    for i in range(1, 20):
        area += 4 * fx_values[i] if i % 2 == 1 else 2 * fx_values[i]

    area *= h / 3
    return area

def main():
    """
    Main function to demonstrate the use of the Probability function.
    """
    # Example 1: Calculate and print the probability P(x < 105 | N(100, 12.5))
    p1 = Probability(GPDF, (100, 12.5), 105, GT=True)
    print("P(x < 105 | N(100, 12.5)) = {:.5f}".format(p1))

    # Example 2: Calculate and print the probability P(x > μ + 2σ | N(100, 3))
    mean = 100
    stDev = 3
    upper_limit = mean + 2 * stDev
    p2 = 1 - Probability(GPDF, (mean, stDev), upper_limit, True)
    print("P(x > {} | N({}, {})) = {:.5f}".format(upper_limit, mean, stDev, p2))


if __name__ == "__main__":
    main()



