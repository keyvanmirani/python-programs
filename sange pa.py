stockQuantity = int(input())
content = []

# get multiple input
for i in range(1, stockQuantity + 1):
    line = int(input())
    content.append(line)


# calculate sales price
def sales(bill_price):
    bill_prices = bill_price
    if len(divisor_counter(bill_price)) == 2:
        sale_price = prime_counter(bill_price)
    else:
        sale_price = prime_divisor(divisor_counter(bill_price))
    bill_price = bill_prices - sale_price
    return bill_price


# check the number is Prime
def price_calculator(wights):
    bill_price = 0
    for wight in wights:
        # print(wight)
        if wight == 1:
            price = 0
        elif len(divisor_counter(wight)) == 2:
            price = prime_counter(wight)
        else:
            price = prime_divisor(divisor_counter(wight))
        bill_price += price
    return bill_price


# prime divisor
def prime_divisor(wights):
    primeArray = []
    for wight in wights:
        if len(divisor_counter(wight)) == 2:
            primeArray.append(wight)

    return len(primeArray)


# count Divisor of number
def divisor_counter(wight):
    divisors = []
    for i in range(1, wight + 1):
        if (wight % i) == 0:
            divisors.append(i)
    return divisors


# count prime number
def prime_counter(wight):
    primesArray = []
    for wight in range(1, wight):
        if wight > 1:
            for i in range(2, wight):
                if (wight % i) == 0:
                    break
            else:
                primesArray.append(wight)
    return len(primesArray)


print(sales(price_calculator(content)))

