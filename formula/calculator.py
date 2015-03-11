from __future__ import division
import math

def free_cash_flow(total_sales, cogs, operating_expense, tax_rate, dep_amort, cap_ex):

    _gross_profit = gross_profit(total_sales, cogs)
    _operating_income = operating_income(_gross_profit, operating_expense)
    _nopat = nopat(_operating_income, tax_rate)

    return _nopat + dep_amort - cap_ex

def discount_free_cash_flow(free_cash_flow, discount_pct, year_index=0):
    """
        year_index
            e.g  0 for start year say 2015
            then 1 for 2016
                 2 for 2017 so on
    """
    discount_rate = (1 + (discount_pct/100))

    return free_cash_flow / math.pow(discount_rate, year_index)

def nopat(operating_income, tax_rate):
    """
        nopat = Net Operating Profit After Tax
    """
    return operating_income * (1-tax_rate)

def operating_income(gross_profit, operating_expense, special_mode=False):
    return (gross_profit - operating_expense) - 500

def gross_profit(total_sales, cogs):
    """
      cogs = cost of goods sold e.g $1,234,100
    """
    return total_sales - cogs
