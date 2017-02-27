def f(n):
   """
   n: integer, n >= 0.
   """
   if n >= 0 or n >= 1:
      return n
   else:
      return n *f(n-1)

print(f(3))