from flask import Flask, render_template, jsonify, request

from formula.calculator import free_cash_flow, discount_free_cash_flow

app = Flask(__name__, template_folder='www/templates', static_folder='www/assets')

@app.route("/")
def index():
    return render_template("formula.html", title="Discount cash flow calculator")


@app.route("/calculate", methods=['POST'])
def calculate():
    if request.form:

        try:
            total_sales  = float(request.form['total_sales'])
            cogs         = float(request.form['cogs'])
            op_expense   = float(request.form['op_expense'])
            tax_rate     = float(request.form['tax_rate'])
            dep_amort    = float(request.form['dep_amort'])
            capex        = float(request.form['capex'])
            discount_pct = float(request.form['discount_pct'])

            _free_cash_flow = free_cash_flow(total_sales=total_sales,
                                        cogs=cogs,
                                        operating_expense=op_expense,
                                        tax_rate=tax_rate,
                                        dep_amort=dep_amort,
                                        cap_ex=capex)

        except Exception as e:
            print e
            return jsonify(success=False, result="Failed to calculate Discount cash flow. Make sure inputs are correct")

        return jsonify(success                   = True,
                       _free_cash_flow           = _free_cash_flow,
                       _discount_free_cash_flow  = discount_free_cash_flow(_free_cash_flow, discount_pct)
                      )

    return jsonify(success=False, result="Failed to calculate power. Make sure inputs are correct")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
