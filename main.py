from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
def sendMessage():
  return {'success': True , 'message' : 'hosting was successful'}
