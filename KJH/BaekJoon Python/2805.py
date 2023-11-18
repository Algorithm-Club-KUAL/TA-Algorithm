from fractions import Fraction
import sympy as sy

Trees,need = map(int,input().split())


lst = list(map(int,input().split()))

x = sy.symbols('x')

eq = sy.Eq(sum(lst)-need ,Trees*x)
print(sy.solve(eq))