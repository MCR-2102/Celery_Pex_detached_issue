.PHONY: build clean

build: buildenv
	. buildenv/bin/activate; python3 setup.py bdist_pex

buildenv:
	python3 -m venv buildenv
	. buildenv/bin/activate; pip3 install -U pip
	. buildenv/bin/activate; pip3 install --no-cache-dir pex wheel requests 
	touch buildenv

clean:
	rm -rf buildenv/
	rm -rf dist/
	rm -rf *.egg-info/

