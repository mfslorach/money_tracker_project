from flask import Flask, render_template
from controllers.transaction_controller import transaction_blueprint

app = Flask(__name__)

app.register_blueprint(transaction_blueprint)

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)