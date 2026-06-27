# COG + MinIO + TiTiler Template

Run:
docker compose up -d

Then upload COGs to the `imagery` bucket in MinIO.

Start API:
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
