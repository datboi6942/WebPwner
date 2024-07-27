from flask import Flask, request, jsonify
import ai
import request_handler
import database

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    method = data.get('method', 'GET')
    vulnerability_type = data.get('vulnerability_type')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    if not vulnerability_type:
        return jsonify({"error": "Vulnerability type is required"}), 400
    
    http_request = ai.generate_http_request(vulnerability_type, url, method)
    
    if not http_request:
        return jsonify({"error": "Failed to generate HTTP request"}), 500
    
    response = request_handler.send_custom_request(http_request)
    if response:
        analysis = ai.analyze_response(response.text)
        responses = [{"http_request": http_request, "analysis": analysis}]
        
        # Store sensitive information if found
        sensitive_info_types = ["LFI", "credentials", "names", "comments", "subdomains", "directories", "locations", "potential vulnerabilities"]
        for info_type in sensitive_info_types:
            if info_type in analysis:
                database.store_sensitive_info(info_type, analysis)
    else:
        responses = [{"http_request": http_request, "error": "Failed to get a response"}]
    
    return jsonify({"results": responses})

if __name__ == '__main__':
    app.run(debug=True)
