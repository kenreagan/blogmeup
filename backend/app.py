from src import create_app, db
import os
from werkzeug.exceptions import HTTPException
import json

app = create_app(config_file='config.ProductionConfig')


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "Error code": e.code,
        "Error Name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
	# perform linear searfch and check for the sqlite db file if created
	for files in os.listdir(os.getcwd()):
		if not files == 'main.sqlite':
			with app.app_context():
				db.create_all()
	app.run()
