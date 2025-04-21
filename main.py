import csv
from math import floor, comb


def probability_of_given_sum(p, n, s):
    coefficient = 1.000 / pow(s, n)
    upper_limit = floor((p - n) / s)
    summation_total = 0
    for k in range(0, upper_limit + 1):
        factor_1 = pow(-1, k)
        factor_2 = comb(n, k)
        factor_3 = comb(p - (s*k) - 1, n - 1)
        summation_total += factor_1 * factor_2 * factor_3
    return coefficient * summation_total


def print_dice_probability_table(n, s):
    with open("output.csv", 'w', newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["number of sides: " + str(s)])
        for nd in range(1, n + 1):
            writer.writerow(["number of dice: " + str(nd)])
            writer.writerow(["p", "p_pns"])
            for p in range(nd, nd * s + 1):
                p_pns = probability_of_given_sum(p, nd, s)
                writer.writerow([p, p_pns])


def main():
    print("dice probability table generator!")
    number_of_sides = 6
    number_of_dice = 4
    print_dice_probability_table(number_of_dice, number_of_sides)
    print("done!")

if __name__ == "__main__":
    main()