def kaprekar(num) :
    i = 0
    while num not in [6174, 0] :
        num = desc_digits(num) - asc_digits(num)
        i += 1
    return i

def breakdown_digits(num) :
    digits = list(map(int, list(str(num))))
    while len(digits) < 4 :
        digits.append(0)
    return digits

def largest_digit(num) :
   return max(breakdown_digits(num))

def asc_digits(num) :
    return int(''.join(map(str, sorted(breakdown_digits(num)))))

def desc_digits(num) :
    return int(''.join(map(str,sorted(breakdown_digits(num), reverse=True))))

print('Largest Digit:')
for num in [1234, 3253, 9800, 3333, 120] :
    print(str(num) + ': ' + str(largest_digit(num)))

print('Descending order:')
for num in [1234, 3253, 9800, 3333, 120] :
    print(str(num) + ': ' + str(desc_digits(num)))

print('Kaprekar:')
for num in [6589, 5455, 6174] :
    print(str(num) + ': ' + str(kaprekar(num)))

# find highest possible output
print('Highest: ' + str(max(map(kaprekar, range(10000)))))

