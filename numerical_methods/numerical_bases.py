#To review / Incomplete

def binToDeci(binary : float) -> float:

  binary_str = str(binary)
  binary_array = binary_str.split(".")

  n = len(binary_array[0]) - 1

  decimal = 0
  for x in binary_str:
    if x == '.':
      continue
    decimal += float(x) *(2 ** n)
    n -= 1

  return decimal

def deciToBin(dec: int) -> str:
    if dec == 0:
        return "0"

    bin_array = []
    quotient = dec

    while quotient > 0:
        rest = quotient % 2
        bin_array.append(str(rest))
        quotient //= 2

    bin_array.reverse()

    bin_str = "".join(bin_array)
    return bin_str
