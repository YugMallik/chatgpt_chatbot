from flask import Flask, request, jsonify
from helper.openai_api import text_complition

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server is running...'


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        result = ''
        data = request.get_json()
        query_text = data['queryResult']['queryText']
        intent = data['queryResult']['intent']['displayName']

        if intent == 'Default Fallback Intent':
            result = text_complition(query_text)

        if result['status'] == 1:
            return jsonify(
                {
                    'fulfillmentText': result['response']
                }
            )
    except:
        pass
    return jsonify(
        {
            'fulfillmentText': 'Something went wrong.'
        }
    )
