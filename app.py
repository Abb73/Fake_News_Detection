# app.py
from flask import Flask, request, render_template,jsonify
from news_predictor import predict
# comment all app
obj=predict()

#text=input('\nEnter text')
#ans=manual_testing(text)
#print('\n',ans)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  
    data = request.json  # Parse the JSON data
    if 'Text' in data:
        Text = data['Text']  # Access the 'Text' key
        ans = obj.manual_testing(Text)
        return jsonify({'prediction': ans})  # Return a JSON response
    else:
        return jsonify({'error': 'Key "Text" not found in request.'}), 400
    
     
    #return str(ans)

if __name__ == '__main__':
    app.run(debug=True)
