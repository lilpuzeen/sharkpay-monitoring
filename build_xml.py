from consts import USDT_CODE, RUB_CODE, DISCOUNT_USDT_RUB, MARKUP_RUB_USDT, DISCOUNT_USDT_OTH
from rapira import fetch_rate
from utils import fmt
from decimal import Decimal, ROUND_HALF_UP
import xml.etree.ElementTree as ET


def build_xml(pairs_cfg) -> str:
    base_rate = fetch_rate()

    rates = ET.Element('rates')
    for p in pairs_cfg:
        frm = p['from']
        to = p['to']
        amount = Decimal(str(p['amount']))
        minamt = Decimal(str(p['minamount']))
        maxamt = Decimal(str(p['maxamount']))

        if frm == USDT_CODE and to == RUB_CODE:
            rate = (base_rate * (Decimal('1') - DISCOUNT_USDT_RUB))
        elif frm == RUB_CODE and to == USDT_CODE:
            inv = (Decimal('1') / base_rate)
            rate = (inv * (Decimal('1') + MARKUP_RUB_USDT))
        elif frm == '{{USDT_CODE}}':
            rate = (base_rate * (Decimal('1') - DISCOUNT_USDT_OTH))
        else:
            rate = fetch_rate()

        rate = rate.quantize(Decimal('0.000001'), ROUND_HALF_UP)

        out_amt = (minamt * rate).quantize(Decimal('0.000001'), ROUND_HALF_UP)

        item = ET.SubElement(rates, 'item')
        ET.SubElement(item, 'from').text = frm.upper()
        ET.SubElement(item, 'to').text = to.upper()
        ET.SubElement(item, 'in').text = fmt(minamt, 2)
        ET.SubElement(item, 'out').text = fmt(out_amt, 6)
        ET.SubElement(item, 'amount').text = fmt(amount, 2)
        ET.SubElement(item, 'minamount').text = f"{fmt(minamt, 2)}"
        ET.SubElement(item, 'maxamount').text = f"{fmt(maxamt, 2)}"

    xml_body = ET.tostring(rates, encoding='utf-8', method='xml').decode('utf-8')
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', xml_body]
    return '\r\n'.join(lines) + '\r\n'
