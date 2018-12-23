# -*- coding: utf-8 -*-
"""
    Obj     : Test whether the given integer is 32 bit signed integer or not.
    Strategy: The limits of a 32 bit signed integer are [-2^31 to +2^31-1] == [−2,147,483,648 to 2,147,483,647] == [-0x80000000 to 0x7fffffff] in hexadecimal format.
              These hexadecimal values will be the masks for checking whether the given number is 32 bit.
              For a +ve number: If you get the same number when you perfom "&" with the upper bound mask...it indicates its a 32 bit.
                                If you get a different number, it means that the number exceeds the limits of 32 bit signed integer
              For a -ve number: When you perform an & with the lower bound mask, and you get the value of lower bound mask...its a 32 bit signed integer
                                If you get a different number, it means that the number exceeds the limits of 32 bit signed integer
"""

# Check limits
print(0x7fffffff)    # Upper bound == 2147483647
print(-0x80000000)   # Lower bound == -2147483648


# Understanding the mask operation [for positive numbers]
num = 123                       
print(num & 0x7fffffff)       # Returns 123

num = 9
print(num & 0x7fffffff)       # Returns 9

num = 19080796876567755777577
print(num & 0x7fffffff)       # Returns 67790377...a different number!...Thus not 32 bit!

# Understanding the mask operation [for negative numbers]
num = -1
print(num & -0x80000000)      # Returns −2,147,483,648

num = -79
print(num & -0x80000000)      # Returns −2,147,483,648

num = -123
print(num & -0x80000000)      # Returns −2,147,483,648

num = 19080796876567755777577
print(num & -0x80000000)       # Returns 19080796876567687987200...a different number..Thus not 32 bit!

