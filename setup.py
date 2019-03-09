
from setuptools import setup
from pathlib import Path

package = 'app'

setup(
	name = 'example_celery',
	include_package_data = True,
	packages = [package],
	install_requires = [
		'flask_bootstrap==3.3.7.1',
		'gunicorn==19.9.0',
		'celery==4.2.1',
	],
	entry_points = {
		'console_scripts': [
			'example.celery.pex = None',
		]
	},
)
