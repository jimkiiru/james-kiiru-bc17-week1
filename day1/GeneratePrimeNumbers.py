#this function generates positive prime numbers in a given range
def GeneratePrimeNumbers(integer_number):
   
    prime_nums = []

    if integer_number in (0, 1):
        return "Zero or One cannot be prime numbers."

    if integer_number < 2:
        return "Not possible to generate prime numbers for integers less than 2."

    if type(integer_number) != int:
        return "Only integers are allowed."

    for n in range(2, integer_number + 1):
        if n > 1:
            for m in range(2, n):
                if (n % m) == 0:
                    break
            else:
                prime_nums.append(n)
    return prime_nums
