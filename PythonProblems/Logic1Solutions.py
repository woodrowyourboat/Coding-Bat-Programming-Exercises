# When squirrels get together for a party, they like to have cigars.
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the number of cigars.
# Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
    success = True

    if 40 <= cigars <= 60 and is_weekend is False:
        return success
    elif cigars >= 40 and is_weekend:
        return success
    else:
        return False


#
#
#
#


def date_fashion(you, date):
    if date <= 2 or you <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


def squirrel_play(temp, is_summer):
    if 60 <= temp <= 90 and is_summer is False:
        return True
    elif 60 <= temp <= 100 and is_summer:
        return True
    else:
        return False


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            return 0
        elif 66 <= speed <= 85:
            return 1
        elif speed >= 86:
            return 2
    elif is_birthday is False:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        elif speed >= 81:
            return 2


def sorta_sum(a, b):
    if 10 <= (a + b) <= 19:
        return 20
    else:
        return a + b


def alarm_clock(day, vacation):
    if vacation:
        if 1 <= day <= 5:
            return "10:00"
        if 0 == day or day <= 6:
            return "off"
    elif vacation is False:
        if 1 <= day <= 5:
            return "7:00"
        elif 0 == day or day <= 6:
            return "10:00"


def love6(a, b):
    if a == 6 or 6 == b:
        return True
    if a + b == 6:
        return True
    elif abs(a - b) == 6:
        return True
    else:
        return False


def in1to10(n, outside_mode):
    if outside_mode:
        if 10 <= n or n <= 1:
            return True
        else:
            return False
    elif outside_mode is False:
        if 1 <= n <= 10:
            return True
        else:
            return False


def near_ten(num):
    remainder_ten = num % 10

    if remainder_ten >= 8 or remainder_ten < 3:
        return True
    else:
        return False
