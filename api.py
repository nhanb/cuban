from bottle import post, run, request

@post('/add/')
def index():
    url = request.params.text
    print(url)
    print(request.params.keys())
    return url


run(host='0.0.0.0', port=8080)
