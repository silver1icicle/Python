"""
Objective: Given a "32-bit signed integer", reverse digits of an integer.
Strategy : Revert the number and then check whether its a 32 bit signed integer.
           The lower and upper bound limits of signed integer: [-2147483648 to 2147483647] == [-0x80000000 to 0x7fffffff]
           Use these limits as a "mask" to test whether the given number lies within the bounds.
           
Reference: https://stackoverflow.com/questions/44581339/reverse-32bit-integer/44582995

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flagNeg=0
        if(x<0):
            flagNeg = 1
        tempX = int(str(abs(x))[::-1])
        if flagNeg == 1:
            tempX *= (-1)

        # Check the 32 bit criterion
        neg_limit = -0x80000000
        pos_limit = 0x7fffffff
        
        if tempX < 0:
            val = tempX & neg_limit
            if(val == neg_limit):
                return tempX
            else:
                return 0
        elif tempX == 0:
            return tempX
        else:
            val = tempX & pos_limit
            if(val == tempX):
                return tempX
            else:
                return 0


            
if __name__ == '__main__':
    obj = Solution()
    print(obj.reverse(123))
    print(obj.reverse(-123))
    print(obj.reverse(-120))
    print(obj.reverse(1534236469))
        
