from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def question():
    return """<html>
                    <head>
                        <style>
                            body{
                                margin-top:5%;
                                margin-left:20%;
                            }
                            h1{
                                color:#51B090;
                                font-size:50px;
                            }
                            p{
                                font-size:25px;
                            }
                            input{
                                font-size:18px;
                            }
                        </style>
                    </head>
                    <body>
                        <h1>Please answer the following question/s:</h1>
                            <form action='/info'>
                                <p>What is your first name?</p><br>
                                <input type='text' name='fname'><br><br>
                                <p>What is your last name?</p><br>
                                <input type='text' name='lname'><br><br>
                                <p>What do you think is your characteristic/s?</p><br>
                                <input type='text' name='characteristic'><br><br><br>
                                <input type='submit' value='Submit'>
                            </form>
                    </body>
            </html>
           """

@app.route('/info')
def info():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    char = request.args['characteristic']
    if char == '':
        msg = "there any problem why you are not answering the form?"
    else:
        msg = char

    return """
        <html><body> 
            <p style="margin-top:20%;text-align:center; font-size:65px;">{0} {1} is {2}<p>
        </body> </html>
           """.format(fname, lname,  msg)

app.run(host="localhost", debug=True)
