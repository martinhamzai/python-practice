import math
import cmath

def get_coefficient(coeff):
    while True:
        try:
            coeff = float(input(f"Enter the {coeff} coefficient: "))
            break
        except:
            print("Invalid. Enter a numerical value.")
    return coeff

def zeros(a, b, c):
    if a == 0:
        print("\nNot a quadratic")
        exit(0)
    try:
        (r, s) = (((-b + math.sqrt(b*b - (4 * a * c))) / 2 * a), 
        ((-b - math.sqrt(b*b - (4 * a * c))) / 2 * a))
    except:
        (r, s) = (complex((-b + cmath.sqrt(b*b - (4 * a * c))) / 2 * a), 
        complex((-b - cmath.sqrt(b*b - (4 * a * c))) / 2 * a))
    return (r, s)

def main():
    print("Quadratic Solver\n")
    a = get_coefficient("First")
    b = get_coefficient("Second")
    c = get_coefficient("Third")

    (r, s) = zeros(a, b, c)
    
    print()
    if type(r) == complex:
        print("The zeros are %g + %gi, %g + %gi" %(r.real, r.imag, s.real, s.imag))
    else:
        print("The zeros are: %g, %g" %(r, s))

if __name__ == "__main__":
    main()