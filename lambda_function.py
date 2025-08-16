from mangum import Mangum
from app import app

lambda_handler = Mangum(app, lifespan="off")
