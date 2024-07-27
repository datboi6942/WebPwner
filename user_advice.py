from flask import Flask, request, jsonify
import ai

app = Flask(__name__)

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    suggestion_type = data.get('suggestion_type')
    suggestion_content = data.get('suggestion_content')
    
    if not suggestion_type or not suggestion_content:
        return jsonify({"error": "Both suggestion_type and suggestion_content are required"}), 400
    
    if suggestion_type == 'payload':
        payloads = ai.generate_payloads(suggestion_content)
        if not payloads:
            return jsonify({"error": "Failed to generate payloads"}), 500
        return jsonify({"payloads": payloads})
    
    elif suggestion_type == 'exploit_vector':
        vectors = ai.suggest_exploit_vectors(suggestion_content)
        if not vectors:
            return jsonify({"error": "Failed to suggest exploit vectors"}), 500
        return jsonify({"exploit_vectors": vectors})
    
    else:
        return jsonify({"error": "Unsupported suggestion type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
