from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route( "/" )
def front_page():
    return render_template( "index.html" )

@app.route( "/process", methods = ["post"])
def process():
    print "Data from form:"
    print request.form
    # print request.form["name"]
    # return render_template( "process.html" )
    return redirect( "/" )

app.run( debug = True )