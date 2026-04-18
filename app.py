from flask import Flask, render_template
from bpPedidos import bpPedidos
from bpFacturas import bpFacturas
 
app = Flask(__name__)
 
app.register_blueprint(bpPedidos)
app.register_blueprint(bpFacturas)
 
@app.route("/")
def index():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)