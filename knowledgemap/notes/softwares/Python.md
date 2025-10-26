# Python 

## Classes

Static Methods can be called without initializing the class. It does not have access to the instance or the class. It is basically a regular python function that is under the class for organizational purpose.

Class methods have access to the class, but not the instance. They can instantiate the class.

Class attributes are like constants, but defined under the class

## Important Note - pass by reference

If you have

def foo(x: torch.Tensor):
    x = x + 1

Even though tensors are pass-by-reference, x is not modified outside of the scope of this function. It is ilik

On the other hand, if you did

def foo(x: torch.Tensor):
    x.add_(1)

The change is seen outside the function


## kwargs
If extra keyword arguments are passed, they go into the kwargs dict. This can be passed again to other inner functions.

Last Reviewed: 4/26/25    

