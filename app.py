from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["POST","GET"])  #added get method to handle get requests
def index():
    
    note = request.form.get("note")      # Changed request.args to request.form to handle the form data
    if note:                             # Checking if the note is empty or not
        notes.append(note)               # Add notes only if it is not empty
        return render_template("home.html", notes=notes) 
    else: 
        return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
