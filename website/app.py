from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/predictor.pickle', 'rb') as f:
    model = pickle.load(f)

def encode_categorical(value, categories):
    """One-hot encode a categorical value"""
    return [1 if value == cat else 0 for cat in categories]

def predict_price(user_input):
    """Predict laptop price using the trained model"""
    # Convert to numpy array and reshape for prediction
    input_array = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    ram = int(request.form.get('ram'))
    weight = float(request.form.get('weight'))
    company = request.form.get('company')
    typename = request.form.get('typename')
    os = request.form.get('os')
    cpu = request.form.get('cpu')
    gpu = request.form.get('gpu')
    ips = int(request.form.get('ips', '0'))
    touchscreen = int(request.form.get('touchscreen', '0'))
    
    # Define categories for each feature
    companies = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Toshiba', 'Other']
    typenames = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
    operating_systems = ['Windows', 'Mac', 'Linux', 'Others']
    cpus = ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD', 'Other']
    gpus = ['Intel', 'AMD', 'Nvidia']
    
    # Create list with all numerical values
    user_input = [
        ram, weight, touchscreen, ips
    ]
    user_input.extend(encode_categorical(company, companies))
    user_input.extend(encode_categorical(typename, typenames))
    user_input.extend(encode_categorical(os, operating_systems))
    user_input.extend(encode_categorical(cpu, cpus))
    user_input.extend(encode_categorical(gpu, gpus))
    
    print(user_input)
    
    # Make prediction
    predicted_price = predict_price(user_input)
    print(f"Predicted Price: {predicted_price}")
    
    # Render result page with prediction and user inputs
    return render_template('result.html', 
                         price=predicted_price,
                         ram=ram,
                         weight=weight,
                         company=company,
                         typename=typename,
                         os=os,
                         cpu=cpu,
                         gpu=gpu,
                         ips=request.form.get('ips', '0'),
                         touchscreen=request.form.get('touchscreen', '0'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)