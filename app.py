
from flask import Flask, jsonify, render_template, request, url_for

def create_app():
    app = Flask(__name__)

    from routes import main
    app.register_blueprint(main)

    return app

app = create_app()

patients = []

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/edit_patient', methods=['PUT'])
def edit_patient():
    data = request.json
    if data is None or 'cpf' not in data:
        return jsonify({'error': 'No input data provided or CPF missing'}), 400
    
    for patient in patients:
        if patient['cpf'] == data['cpf']:
            patient.update({
                'name': data.get('name', patient['name']),
                'condition': data.get('condition', patient['condition']),
                'date': data.get('date', patient['date']),
                'paid': data.get('paid', patient['paid'])
            })
            return jsonify(patient)
    
    return jsonify({'error': 'Patient not found'}), 404

@app.route('/delete_patient', methods=['DELETE'])
def delete_patient():
    data = request.json
    if data is None or 'cpf' not in data:
        return jsonify({'error': 'No input data provided or CPF missing'}), 400
    
    global patients
    patients = [patient for patient in patients if patient['cpf'] != data['cpf']]
    return jsonify({'result': 'Patient deleted'})

@app.route('/get_patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    if data is None:
        return jsonify({'error': 'No input data provided'}), 400
    if not all(key in data for key in ('cpf', 'name', 'condition', 'date', 'paid')):
        return jsonify({'error': 'Missing required data'}), 400

    patient = {
        'cpf': data['cpf'],
        'name': data['name'],
        'condition': data['condition'],
        'date': data['date'],
        'paid': data['paid']
    }
    patients.append(patient)
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
