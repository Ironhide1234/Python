def factorial(n):
    numbers = [1]
    def find():
        while n > len(numbers):
            numbers.append((len(numbers)+1) * numbers[len(numbers)-1])
        return numbers[n-1]
    return find


x = factorial(5)
print(x())
