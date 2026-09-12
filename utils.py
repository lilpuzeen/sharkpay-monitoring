from decimal import Decimal, ROUND_HALF_UP


def fmt(d: Decimal, prec: int) -> str:
    """d округляем до prec знаков после запятой"""
    q = '1.' + ('0'*prec)
    return format(d.quantize(Decimal(q), ROUND_HALF_UP), 'f')
