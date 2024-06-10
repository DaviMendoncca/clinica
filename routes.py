from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('homepage.html')

@main.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@main.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

# Rota para listar todas as rotas (para debugging)
@main.route('/routes')
def list_routes():
    from flask import jsonify
    import urllib
    output = []
    for rule in main.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)
    return jsonify(output)
