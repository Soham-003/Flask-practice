from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route("/calculate",methods = ["GET","POST"])
def display():
    if request.method == "GET" :
        return render_template('index.html')
    else :
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        opr = request.form['operation']
        if(opr == 'addition') : result = num1 + num2
        if(opr == 'multiplication') : result = num1 * num2
        if(opr == 'subtraction') : result = num1 - num2
        if(opr == 'division') : result = num1 / num2
    return render_template('result.html',num1 = num1,num2 = num2,operation = opr,result = result)  

@app.route("/Postman_API",methods = ["POST"])
def calculator():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)

if __name__ == "__main__": 
   app.run(debug = True)