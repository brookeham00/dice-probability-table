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
    print("p_pns, p, sides, dice")
    for p in range(n, n * s + 1):
        p_pns = probability_of_given_sum(p, n, s)
        print(str(p_pns) + ", " + str(p) + ", " + str(s) + ", " + str(n))


def main():
    print("dice probability table generator!")
    number_of_sides = 6
    number_of_dice = 2
    print_dice_probability_table(number_of_dice, number_of_sides)

if __name__ == "__main__":
    main()