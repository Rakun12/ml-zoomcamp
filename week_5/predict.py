import pickle

input_file = 'model_C=1.bin'

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# For testing
customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('input', customer)
print('\nchurn probability :', y_pred)
