"""Send greetings."""
import sys


def greet(name):
    return f"Hello, {name}."


def run(args=None):
    """Process console line arguments."""
    if not args:
        args = sys.argv[1:]
    name = args[0]
    print(greet(name))
