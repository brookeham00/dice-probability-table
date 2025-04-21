def probability_of_given_sum(p, number_of_dice, number_of_sides):
    return p + number_of_dice + number_of_sides #NOT THE REAL FORMULA


def print_dice_probability_table(number_of_dice, number_of_sides):
    print("p_pns, p, sides, dice")
    for p in range(number_of_dice, number_of_dice * number_of_sides + 1):
        p_pns = probability_of_given_sum(p, number_of_dice, number_of_sides)
        print(str(p_pns) + ", " + str(p) + ", " + str(number_of_sides) + ", " + str(number_of_dice))


def main():
    print("dice probability table generator!")
    number_of_sides = 5
    number_of_dice = 3
    print_dice_probability_table(number_of_dice, number_of_sides)

if __name__ == "__main__":
    main()