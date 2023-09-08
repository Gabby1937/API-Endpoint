from flask import Flask, jsonify, request
from datetime import datetime
import pytz


app = Flask(__name__)

@app.route('/path', methods=['GET'])
def details():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    current_day = datetime.now(pytz.UTC).strftime('%A')
    present_time = datetime.now(pytz.UTC)
    
    time_diff = current_day.utcoffset().total_seconds() / 3600
    time_validation = 'within +/-2 hours'
    if time_diff < -2 or time_diff > 2:
        time_validation = 'outside +/-2 hours'
        
    git_file = 'https://github.com/Gabby1937/API-Endpoint.git'
    git_repo = 'https://github.com/Gabby1937/API-Endpoint.git'
    
    response = {
        "slack_name": slack_name,
        "track": track,
        "current_day": current_day,
        "utc_time" : present_time.strftime('%y-%m-%d %H:%M:%S UTC'),
        "time_validation": time_validation,
        "github_file_url" : git_file,
        "github_repo_url" : git_repo,
        "status code": 200
    }
    return jsonify(response)
    


if __name__ == "__main__":
    app.run(debug=True)#, #host='0.0.0.0', port=5000)