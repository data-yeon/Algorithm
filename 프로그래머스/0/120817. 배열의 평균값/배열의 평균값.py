from decimal import Decimal, ROUND_HALF_UP
def solution(numbers):
    avg = Decimal(sum(numbers)) / Decimal(len(numbers))
    
    half = (avg * 2).quantize(Decimal('1'), rounding = ROUND_HALF_UP) /Decimal(2)
    return float(half)