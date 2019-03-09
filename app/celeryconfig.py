import os


broker_dir = '/tmp/broker'

if not os.path.exists(broker_dir):
	os.makedirs(broker_dir)

broker_url = 'filesystem://'
broker_transport_options = {
	'data_folder_in': os.path.join(broker_dir, 'out'),
	'data_folder_out': os.path.join(broker_dir, 'out'),
	'data_folder_processed': os.path.join(broker_dir, 'processed')
}
imports = ('app.tasks',)
result_persistant = False
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
timezone = 'Europe/London'

beat_schedule = {
	'task_schedule_name_mr': {
		'task': 'long_running_task',
		'schedule':30.0
	},
}
