from flask import Flask, request, jsonify, render_template, url_for

def create_app():
    app = Flask(__name__)

    from routes import main
    app.register_blueprint(main)

    return app

app = create_app()


patients = []




@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    patient = {
        'cpf': data['cpf'],
        'name': data['name'],
        'condition': data['condition'],
        'date': data['date'],
        'paid': data['paid'],
    }
    patients.append(patient)
    return jsonify(patients)

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

