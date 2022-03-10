"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def _subquadratic_multiply(x, y):
  xvec, yvec = pad(x.binary_vec, y.binary_vec)
  #if(len(xvec) <= 1 and len(yvec) <= 1):
  if(x.decimal_val <= 1 and y.decimal_val <= 1):
    return BinaryNumber(x.decimal_val*y.decimal_val)
  else:
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    n = len(xvec)
    #left part
    LP = _subquadratic_multiply(x_left, y_left)
    sumLeft = bit_shift(LP, n)

    #right sum
    sumRight = _subquadratic_multiply(x_right, y_right)

    #middle sum
    MsumL = _subquadratic_multiply(BinaryNumber(x_left.decimal_val+x_right.decimal_val), BinaryNumber(y_left.decimal_val+y_right.decimal_val))
    inside = MsumL.decimal_val - LP.decimal_val - sumRight.decimal_val
    sumMid = bit_shift(BinaryNumber(inside), n//2)

    total = sumLeft.decimal_val + sumMid.decimal_val + sumRight.decimal_val
    return BinaryNumber(total)

def subquadratic_multiply(x, y):
  #converts the result from a binary number to a regular int
  return _subquadratic_multiply(x, y).decimal_val


def time_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  subquadratic_multiply(x, y)
  return (time.time() - start)*1000

## Feel free to add your own tests here.
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert subquadratic_multiply(BinaryNumber(8), BinaryNumber(5)) == 8*5
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(15)) == 20*15
  assert subquadratic_multiply(BinaryNumber(42), BinaryNumber(31)) == 42*31
  
print(time_multiply(BinaryNumber(2), BinaryNumber(2), subquadratic_multiply))
print(time_multiply(BinaryNumber(20), BinaryNumber(20), subquadratic_multiply))
print(time_multiply(BinaryNumber(200), BinaryNumber(200), subquadratic_multiply))
print(time_multiply(BinaryNumber(2000), BinaryNumber(2000), subquadratic_multiply))
print(time_multiply(BinaryNumber(20000), BinaryNumber(20000), subquadratic_multiply))
print(time_multiply(BinaryNumber(200000), BinaryNumber(200000), subquadratic_multiply))
print(time_multiply(BinaryNumber(2000000), BinaryNumber(2000000), subquadratic_multiply))


    

