from flask import Flask,render_template_string

app= Flask (__name__)

@app.route("/")
def loginnn():
    return ("loginnn.html")


@app.route('/alu.html')
def alu():
    return ('alu.html')

if __name__ == '__main__':
    app.run(debug=True)