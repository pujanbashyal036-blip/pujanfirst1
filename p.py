def average_score(x, n):
    return (x / n)

def strike_rate(x, y):
    if y == 0:
        return "Error! Division by zero."
    return (x / y) * 100

def main():
    n = int(input("enter a number of match"))
    x = 0
    y = 0
    for i in range(n):
        a = int(input(f"number of score in match {i+1}: "))
        b = int(input(f"number of ball in match {i+1}: "))
        x += a
        y += b
    print("Match", n, "Score:", x, "Balls:", y)
    print("Average Score:", average_score(x, n))
    print("Strike Rate:", strike_rate(x, y))


