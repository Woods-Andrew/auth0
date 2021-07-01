from flask import Flask, request

app = Flask(__name__)

@app.route('/headers')
def headers():
    # @TODO unpack the request header
    auth_header = request.headers['Authorization']
    header_parts = auth_header.spilt(' ')[1]

    print(header_parts)
    return 'not implemented'
