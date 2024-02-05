from math import cos


def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Find the root of a function using the Secant method.

    Args:
    - fcn (function): The function for which the root is to be found.
    - x0 (float): Initial guess 1.
    - x1 (float): Initial guess 2.
    - maxiter (int): Maximum number of iterations (default is 10).
    - xtol (float): Tolerance for stopping criterion (default is 1e-5).

    Returns:
    tuple: The root and the number of iterations taken.
    """
    iterations = 0
    x_previous = x0
    x_current = x1

    while iterations < maxiter:
        f_previous = fcn(x_previous)
        f_current = fcn(x_current)

        if abs(x_current - x_previous) < xtol:
            return x_current, iterations

        # Secant method formula
        x_new = x_current - (f_current * (x_current - x_previous)) / (f_current - f_previous)

        x_previous = x_current
        x_current = x_new

        iterations += 1

    return x_current, iterations


def main():
    """
    Main function to demonstrate the use of the Secant method for finding roots.
    """
    # Example 1: Finding root for x - 3 * cos(x)
    fcn1 = lambda x: x - 3 * cos(x)
    root1 = Secant(fcn1, 1, 2, maxiter=5, xtol=1e-4)
    print("Root 1:", root1[0])
    print("Iterations:", root1[1])

    # Example 2: Finding root for cos(2 * x) * x^3
    fcn2 = lambda x: cos(2 * x) * x**3
    root2 = Secant(fcn2, 1, 2, maxiter=15, xtol=1e-8)
    print("Root 2:", root2[0])
    print("Iterations:", root2[1])

    # Example 3: Finding root for cos(2 * x) * x^3 with a lower iteration limit
    fcn3 = lambda x: cos(2 * x) * x**3
    root3 = Secant(fcn3, 1, 2, maxiter=3, xtol=1e-8)
    print("Root 3:", root3[0])
    print("Iterations:", root3[1])


if __name__ == "__main__":
    main()



