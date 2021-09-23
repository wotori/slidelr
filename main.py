import fastapi
import uvicorn
import subprocess

app = fastapi.FastAPI()

@app.get('/right')
def left():
    bash_command = "xdotool key Right"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, errors = process.communicate()
    return output, errors

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
