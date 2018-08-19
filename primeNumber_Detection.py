#prime number detector (For numbers less than 10201)

import math
import numpy as np

prime_numbers = np.array([2,3,5,7,11.13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101])

def primeDetector(p):
    
    """Function starts here"""
    
    if (p > 10201):
        raise ValueError("greater than 10201, enter a smaller number")
    
    if p < 100 and p in prime_numbers:
        return ("{} is a prime number".format(p))
    else:
        sq_p = math.sqrt(p)
        near_gt = math.ceil(sq_p)
        lessThan_num = prime_numbers[prime_numbers < near_gt]
        final_Ans = ['No' if (p%i) == 0 else "Yes" for i in lessThan_num]
        final_Ans = list(set(final_Ans))
        if (len(final_Ans) == 1 and final_Ans[0] == 'Yes'):
            return ("{} is a prime number".format(p))
        else:
            return ("{} is not a prime number".format(p))
    
if __name__ == '__main__':
    p = int(input())
    print (primeDetector(p))

    