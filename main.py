from flask import Flask, render_template, send_from_directory
import os
import response_analysis
import user_advice

app = Flask(__name__, static_folder='frontend/build', template_folder='frontend/build')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

# Register blueprints from other modules
app.register_blueprint(response_analysis.app, url_prefix='/api')
app.register_blueprint(user_advice.app, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
