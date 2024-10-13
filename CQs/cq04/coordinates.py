"""Importing CQ - coordinates."""

__author__ = "730652750"


def get_coords(xs: str, ys: str) -> None:
    index = 0
    while index < len(xs):
        coord = 0
        while coord < len(ys):
            print((xs[index], ys[coord]))
            coord += 1
        index += 1
