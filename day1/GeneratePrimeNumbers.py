
def GeneratePrimeNumbers(integer_number):
   
    prime_nums = []

    if integer_number in (0, 1):
        return "Zero or One cannot be prime numbers."

    if integer_number < 2:
        return "Not possible to generate prime numbers for integers less than 2."

    if type(integer_number) != int:
        return "Only integers are allowed."

    for i in range(2, integer_number + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_nums.append(i)
    return prime_nums
