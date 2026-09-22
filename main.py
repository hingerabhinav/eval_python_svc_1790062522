from fastapi import FastAPI

app = FastAPI(title="eval_python_svc_1790062522")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "eval_python_svc_1790062522", "owner": "eval_team_1790062522"}
