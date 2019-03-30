#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#this is a solution of https://www.codewars.com/kata/576757b1df89ecf5bd00073b

# -- coding: utf-8 --

def tower_builder(n_floors):
    return [
        "{}{}{}".format(i * " ", j * "*", i * " ")
        for i, j in zip(
            range(n_floors -1, -2, -1),
            range(1, n_floors * 2, 2)
            )
    ]


if __name__ == "__main__":
    print(
        '\n'.join(tower_builder(7))
    )