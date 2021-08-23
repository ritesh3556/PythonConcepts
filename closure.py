# Closure & first class function-------->
def to_power(x):
    def calc(n):
        return n**x
    return calc

Square = to_power(2)
print(square(4))