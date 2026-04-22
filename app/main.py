from fastapi import FastAPI


app = FastAPI(title="FastAPI deploy")


@app.get('/')
async def main():
    return {'message': 'project is running...'}