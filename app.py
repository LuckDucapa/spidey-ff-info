from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Target API Configuration
TARGET_API = "https://danger-info-alpha.vercel.app/accinfo"
API_KEY = "DANGERxINFO"
CREDIT_TEXT = "\n\nJSON credit: https://t.me/spidey_abd"

@app.route('/info', methods=['GET'])
def get_info():
    # 1. Get UID from the URL
    uid = request.args.get('uid')
    
    if not uid:
        return Response("Error: Missing 'uid' parameter.", status=400, mimetype='text/plain')

    # 2. Construct the Target URL
    # format: url?uid={uid}&key={key}
    final_url = f"{TARGET_API}?uid={uid}&key={API_KEY}"

    try:
        # 3. Fetch data
        response = requests.get(final_url)
        
        # 4. Append Credit
        output = response.text + CREDIT_TEXT
        
        # 5. Return result
        return Response(output, mimetype='text/plain')

    except Exception as e:
        return Response(f"Server Error: {str(e)}", status=500, mimetype='text/plain')

# Simple 404 for Home Page (since you said no home page)
@app.route('/')
def home():
    return Response("Spidey FF Info API is Running. Use /info?uid=...", mimetype='text/plain')

if __name__ == '__main__':
    app.run()
