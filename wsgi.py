from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)
@app.route("/")
def my_home():
    return render_template("index.html" )

@app.route("/<string:page>")
def my_works(page=None):
    return render_template(page)

def write_csv(data):
    with open('database.csv' , newline = '' , mode = 'a') as database:
        csv_data = csv.writer(database, delimiter=','
,quotechar = ',',quoting=csv.QUOTE_MINIMAL)
        csv_data.writerow([data['email'],data['subject'],data['message']])

@app.route('/submit_form', methods=['POST', 'GET'])
def  submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_csv(data)
            return redirect('/thank.html')
        except:
            return 'did not save''
    else:
        return 'WRONG'
