import time
import matplotlib.pyplot as plt

PROBLEM_SIZE = 40

'''
Fibonacci iterative solution

Time: O(n)
Space: O(1)
'''
def fibIter(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

'''
Fibonacci recursive solution
Time: O(2^n)
Space: O(n)
'''
def fibRecur(n):
    if n <= 1:
        return n
    else:
        return fibRecur(n-1) + fibRecur(n-2)
    
def main():
    print("Fibonacci comparision \n")

    # Iterative
    start = time.time()
    fib = fibIter(PROBLEM_SIZE)
    end = time.time()
    print(f"Iterative: {fib}")
    print("%.7f seconds" %(end - start))

    print()

    # Recursive
    start = time.time()
    fib = fibRecur(PROBLEM_SIZE)
    end = time.time()
    print(f"Recursive: {fib}")
    print ("%.7f seconds" %(end - start))

    # Take times from F_0 to F_n
    iter = []
    for i in range(PROBLEM_SIZE + 1):
        start = time.time()
        fibIter(i)
        end = time.time()
        iter.append(end - start)

    recur = []
    for i in range(PROBLEM_SIZE + 1):
        start = time.time()
        fibRecur(i)
        end = time.time()
        recur.append(end - start)

    # plot
    plt.plot(iter, label = "Iterative")
    plt.plot(recur, label = "Recursive")
    plt.xlabel("Iteration")
    plt.ylabel("Time (Seconds)")
    plt.legend()
    plt.title("Iterative vs Recursive Fibonacci Sequence")
    plt.show()


if __name__ == "__main__":
    main()