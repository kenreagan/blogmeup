from src import create_app, db
import os

app = create_app(config_file='config.ProductionConfig')


if __name__ == '__main__':
	# perform linear searfch and check for the sqlite db file if created
	for files in os.listdir(os.getcwd()):
		if not files == 'main.sqlite':
			with app.app_context():
				db.create_all()
	app.run()
