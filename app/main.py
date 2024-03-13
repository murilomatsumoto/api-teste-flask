from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    impact = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    itilcategories_id = db.Column(db.Integer, nullable=False)
    locations_id = db.Column(db.Integer, nullable=False)

@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    data = request.json

    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    input_data = data.get('input')

    if input_data is None:
        return jsonify({'error': 'Input data not provided'}), 400

    name = input_data.get('name')
    content = input_data.get('content')
    urgency = input_data.get('urgency')
    impact = input_data.get('impact')
    priority = input_data.get('priority')
    itilcategories_id = input_data.get('itilcategories_id')
    locations_id = input_data.get('locations_id')

    # Criar um novo ticket
    new_ticket = Ticket(name=name, content=content, urgency=urgency, impact=impact,
                        priority=priority, itilcategories_id=itilcategories_id,
                        locations_id=locations_id)
    
    # Adicionar e commit ao banco de dados
    db.session.add(new_ticket)
    db.session.commit()

    return jsonify({
        'name': name,
        'content': content,
        'urgency': urgency,
        'impact': impact,
        'priority': priority,
        'itilcategories_id': itilcategories_id,
        'locations_id': locations_id
    }), 200

@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    ticket_data = []
    for ticket in tickets:
        ticket_data.append({
            'id': ticket.id,
            'name': ticket.name,
            'content': ticket.content,
            'urgency': ticket.urgency,
            'impact': ticket.impact,
            'priority': ticket.priority,
            'itilcategories_id': ticket.itilcategories_id,
            'locations_id': ticket.locations_id
        })
    return jsonify({'tickets': ticket_data}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port =6000, debug=True)
