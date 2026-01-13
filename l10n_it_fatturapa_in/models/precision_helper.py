# -*- coding: utf-8 -*-
# Copyright 2025 Cogito Srl
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

"""
Helper functions for decimal precision with fallback mechanism.
These functions provide dynamic precision for e-invoice fields,
using dedicated precision if available, otherwise falling back to standard ones.
"""


def get_einvoice_in_quantity_precision(cr):
    """
    Get precision for incoming e-invoice quantity with fallback.

    Uses 'E-Invoice IN Quantity' if available, otherwise falls back to
    'Product Unit of Measure'.

    :param cr: database cursor
    :return: tuple (total_digits, decimal_digits)
    """
    try:
        cr.execute(
            "SELECT digits FROM decimal_precision WHERE name=%s",
            ('E-Invoice IN Quantity',)
        )
        res = cr.fetchone()
        if res:
            return (16, res[0])
    except Exception:
        pass

    # Fallback to standard precision
    try:
        cr.execute(
            "SELECT digits FROM decimal_precision WHERE name=%s",
            ('Product Unit of Measure',)
        )
        res = cr.fetchone()
        if res:
            return (16, res[0])
    except Exception:
        pass

    # Ultimate fallback
    return (16, 3)


def get_einvoice_in_price_precision(cr):
    """
    Get precision for incoming e-invoice unit price with fallback.

    Uses 'E-Invoice IN Unit Price' if available, otherwise falls back to
    'Product Price'.

    :param cr: database cursor
    :return: tuple (total_digits, decimal_digits)
    """
    try:
        cr.execute(
            "SELECT digits FROM decimal_precision WHERE name=%s",
            ('E-Invoice IN Unit Price',)
        )
        res = cr.fetchone()
        if res:
            return (16, res[0])
    except Exception:
        pass

    # Fallback to standard precision
    try:
        cr.execute(
            "SELECT digits FROM decimal_precision WHERE name=%s",
            ('Product Price',)
        )
        res = cr.fetchone()
        if res:
            return (16, res[0])
    except Exception:
        pass

    # Ultimate fallback
    return (16, 2)
