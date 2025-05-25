import os
from decimal import Decimal

markup_percent = os.getenv("MARKUP_PERCENT")
markup_percent_oth = os.getenv("MARKUP_PERCENT_OTH")


DISCOUNT_USDT_RUB = Decimal(markup_percent) / Decimal('100')
MARKUP_RUB_USDT   = Decimal(markup_percent) / Decimal('100')
DISCOUNT_USDT_OTH = Decimal(markup_percent_oth) / Decimal('100')

USDT_CODE = str(os.getenv("USDT_CODE"))
RUB_CODE = str(os.getenv("RUB_CODE"))
