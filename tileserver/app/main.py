from fastapi import FastAPI
from titiler.core.factory import TilerFactory

app=FastAPI(title="COG XYZ Service")

cog=TilerFactory(router_prefix="/cog")
app.include_router(cog.router)

@app.get("/")
def root():
    return {
      "message":"COG XYZ Service",
      "example":"http://localhost:8000/cog/tiles/{z}/{x}/{y}?url=s3://imagery/ortho.tif"
    }
