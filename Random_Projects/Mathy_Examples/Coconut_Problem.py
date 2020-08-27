# 5 sailors shipwrecked and a monkey
# 1st sailor is able to divide into 5 with one left oveer
# 2nd sailor is able to divide into 5 with one left oveer
# 3rd sailor is able to divide into 5 with one left oveer
# 4th sailor is able to divide into 5 with one left oveer
# 5th sailor is able to divide into 5 with one left oveer
# Final pile goes evenly five ways



original_guess = 1
solution = False
while solution is False:
    original_guess += 1
    if original_guess % 500 == 0:
        print('Just tried: %s' % original_guess)
    if original_guess % 5 == 1:
        pile_size = original_guess - ((original_guess - 1) / 5) - 1
        if pile_size % 5 == 1:
            pile_size -= (((pile_size - 1) / 5) + 1)
            if pile_size % 5 == 1:
                pile_size -= (((pile_size - 1) / 5) + 1)
                if pile_size % 5 == 1:
                    pile_size -= (((pile_size - 1) / 5) + 1)
                    if pile_size % 5 == 1:
                        pile_size -= (((pile_size - 1) / 5) + 1)
                        if pile_size % 5 == 1:
                            print('The solution is: %s' % original_guess)
                            solution = True
