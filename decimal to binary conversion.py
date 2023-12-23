def decimal_to_binary(n):

  binary = []
  while n > 0:
    binary.append(n % 2)
    n //= 2
  binary.reverse()
  return "".join(str(i) for i in binary)


print(decimal_to_binary(10))  # 1010
print(decimal_to_binary(52))  # 110100
print(decimal_to_binary(74))  # 1001010
