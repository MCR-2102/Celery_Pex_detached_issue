import os
from celery import Celery

import app.celeryconfig as celeryconfig

from celery.schedules import crontab

print("In app.worker.py")

broker_dir = '/tmp/broker'

if not os.path.exists(broker_dir):
	os.makedirs(broker_dir)

for f in ['out', 'processed']:
	if not os.path.exists(os.path.join(broker_dir, f)):
		os.makedirs(os.path.join(broker_dir, f))

app = Celery(__name__)

app.config_from_object(celeryconfig)

def main():
	print("In worker.py main()")
	pass

if __name__ == "__main__":
	main()
