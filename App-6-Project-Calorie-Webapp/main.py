from os import name

from flask import Flask, render_template, request
from flask.views import MethodView
from flatmates_bill import flat
from wtforms import Form, StringField, SubmitField

# __name__ refers to the python file
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        amount = bill_form.amount.data
        period = bill_form.period.data

        name1 = bill_form.name1.data
        days_in_house1 = bill_form.days_in_house1.data

        name2 = bill_form.name2.data
        days_in_house2 = bill_form.days_in_house2.data

        the_bill = flat.Bill(float(amount), period)
        flatemate1 = flat.Flatmate(name1, float(days_in_house1))
        flatemate2 = flat.Flatmate(name2, float(days_in_house2))
        return render_template(
            "bill_form_page.html",
            result=True,
            name1=flatemate1.name,
            name2=flatemate2.name,
            amount1=flatemate1.pays(the_bill, flatemate2),
            amount2=flatemate1.pays(the_bill, flatemate1),
            billform=bill_form,
        )


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=110)
    period = StringField("Period: ", default="Dec 25")

    name1 = StringField("Name: ", default="Lu")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Yang")
    days_in_house2 = StringField("Days in the house: ", default=25)

    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))

app.run(debug=True)
