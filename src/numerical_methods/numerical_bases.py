def binToDeci(binary: str) -> float:
  binary_parts: list[str] = binary.split(".")
  integer_part: str = binary_parts[0]
  fractional_part: str = binary_parts[1] if len(binary_parts) > 1 else ""

  decimal: float = sum(int(bit) * (2**i) for i, bit in enumerate(reversed(integer_part)))
  decimal += sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(fractional_part))
  return decimal

def deciToBin(decimal: str) -> str:
  decimal_parts: list[str] = decimal.split(".")
  integer_part = int(decimal_parts[0])
  fractional_part: float = float("0." + decimal_parts[1]) if len(decimal_parts) > 1 else 0.0

  binary_integer: str = bin(integer_part)[2:]
  binary_fractional: list[str] = []
  while fractional_part > 0 and len(binary_fractional) < 64:
      fractional_part *= 2
      bit = int(fractional_part)
      binary_fractional.append(str(bit))
      fractional_part -= bit
  return (f"{binary_integer}.{''.join(binary_fractional)}" if binary_fractional else binary_integer)
