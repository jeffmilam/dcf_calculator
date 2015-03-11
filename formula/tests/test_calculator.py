import unittest
from formula.calculator import free_cash_flow, gross_profit, operating_income, nopat, \
        discount_free_cash_flow

class TestDcfCalculatorYear2014(unittest.TestCase):

    def test_gross_profit(self):
        self.assertEquals(gross_profit(total_sales=1477600,cogs=1235100), 242500)

    def test_operating_income(self):
        _gross_profit = gross_profit(total_sales=1477600,cogs=1235100)

        self.assertEquals(operating_income(_gross_profit, operating_expense=180700, adjustment=500), 61300)

    def test_nopat(self):

        _operating_income = operating_income(gross_profit(total_sales=1477600,cogs=1235100), 180700,  adjustment=500)

        self.assertEquals(nopat(_operating_income, 0), 61300)

    def test_free_cash_flow(self):
        self.assertEquals(free_cash_flow(total_sales=1477600,
                                    cogs=1235100,
                                    operating_expense=180700,
                                    tax_rate=0,
                                    dep_amort=58100,
                                    cap_ex=62200,
                                    adjustment=500), 57200)


    def test_discount_free_cash_flow(self):
        _free_cash_flow = free_cash_flow(total_sales=1477600,
                                    cogs=1235100,
                                    operating_expense=180700,
                                    tax_rate=0,
                                    dep_amort=58100,
                                    cap_ex=62200,
                                    adjustment=500)

        self.assertEquals(discount_free_cash_flow(_free_cash_flow, 10, 0), 57200)

class TestDcfCalculatorYear2015(unittest.TestCase):

    def test_gross_profit(self):
        self.assertEquals(gross_profit(total_sales=1507152,cogs=1260733), 246419)

    def test_operating_income(self):
        _gross_profit = gross_profit(total_sales=1507152,cogs=1260733)

        self.assertEquals(operating_income(_gross_profit, operating_expense=182365, adjustment=0), 64054)

    def test_nopat(self):

        _operating_income = operating_income(gross_profit(total_sales=1507152,cogs=1260733), operating_expense=182365,  adjustment=0)

        self.assertEquals(nopat(_operating_income, 0), 64054)

    def test_free_cash_flow(self):
        self.assertEquals(free_cash_flow(total_sales=1507152,
                                    cogs=1260733,
                                    operating_expense=182365,
                                    tax_rate=0,
                                    dep_amort=52100,
                                    cap_ex=55000,
                                    adjustment=0), 61154)


    def test_discount_free_cash_flow(self):
        _free_cash_flow = free_cash_flow(total_sales=1477600,
                                    cogs=1235100,
                                    operating_expense=180700,
                                    tax_rate=0,
                                    dep_amort=58100,
                                    cap_ex=62200,
                                    adjustment=500)

        self.assertEquals(discount_free_cash_flow(_free_cash_flow, 10, 0), 57200)

