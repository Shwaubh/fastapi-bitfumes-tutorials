from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    resp = dict()
    resp['name'] = 'Saurabh'
    resp['name'] = 'Saurabh Giri'
    resp['Name'] = 'SKG'
    return resp

@app.get('/about')
def about():
    resp = {}
    resp['data'] = 'This is the detail of about page'
    return resp