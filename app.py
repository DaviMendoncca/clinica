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

@app.route('/get_patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

