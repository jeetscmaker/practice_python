import time as t
for x in range(10):
    print(x)  # it will print from 0 to 9.

for x in range(1, 11):
    print(x)  # it will print from 1 to 10

for x in range(1, 20, 2):  # it means from 1 to 19 by taking 2 steps
    print(x)  # prints 1 3 5 7...19

# Calculate the factorial of n.
# fac(n) = 1*2*3*.....*n


def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


print(fac(5))

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
for av, bv in zip(a, b):
    print(av, bv)

for index, (av, bv) in enumerate(zip(a, b)):
    print(f"{index}-> {av}, {bv}")

# measuring the performance time of factorial algorithm
start_time = t.perf_counter_ns()
print(fac(10))
end_time = t.perf_counter_ns()
print(f"The time taken to run factorial algorithm: {(end_time-start_time)/1000000} milli-sec")
