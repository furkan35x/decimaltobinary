def decimal_to_binary(n):

  binary = []
  while n > 0:
    binary.append(n % 2)
    n //= 2
  binary.reverse()
  return "".join(str(i) for i in binary)


print(decimal_to_binary(79))  # 1010
print(decimal_to_binary(46))  # 1100
print(decimal_to_binary(22))  # 10000
