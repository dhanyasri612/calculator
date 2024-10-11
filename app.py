from flask import Flask, render_template, request,jsonify

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('design.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from the request
    data = request.json
    expression = data.get('expression')
    
    try:
        # Evaluate the expression safely
        result = eval(expression)
    except Exception as e:
        result = f'Error: {str(e)}'
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)