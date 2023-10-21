import mysql.connector
from flask import Flask, request, jsonify
Database = mysql.connector.connect(host='localhost', user='root', password='', database='project')
app = Flask(__name__)

@app.route('/guestEntry/<string:fName>/<string:lName>/<string:mobileNumber>/<string:dateOfBirth>', methods=["POST", "GET"])
def guestEntry(fName, lName, mobileNumber, dateOfBirth):
    cur = Database.cursor()
    s = "Insert into Entries (FirstName, LastName, MobileNumber, Dateandtime) Values(%s,%s,%s,%s)"
    t = (fName, lName, mobileNumber, dateOfBirth)
    cur.execute(s,t)
    Database.commit()
    return 'Done'


if __name__ == "__main__":
    app.run(debug=True)
