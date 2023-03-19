from fastapi import FastAPI'

app = FastApi()

@app.get('')
def sendMessage():
  return {'success': True , 'message' : 'hosting was successful'}
