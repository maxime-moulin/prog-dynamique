# Author: Bishal Sarang, https://github.com/Bishalsarang/Recursion-Tree-Visualizer/

import sys

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs
@vs(
    show_return_value=True,
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "grey",
    },
)
def fib(n):
    if n <= 1:
        return n
    return fib(n=n - 1) + fib(n=n - 2)


def main(n=4, delay=1.5):
    # Call function
    print(fib(n=n))
    # Save recursion tree to a file
    vs.make_animation(f"fibonacci-{n}.gif", delay=delay)

if __name__ == "__main__":
    n = 4
    delay = 1.5
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        delay = float(sys.argv[2])

    main(n, delay)
