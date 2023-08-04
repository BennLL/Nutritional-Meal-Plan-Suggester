from flask import Flask, request, render_template

from chatGPT import act_as

app = Flask(__name__, template_folder='')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/advice', methods=['POST'])
def chatbot():

    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return {'message': "Please enter a valid message."}

    response_message = act_as(user_prompt=user_message)

    return {'message': response_message}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
