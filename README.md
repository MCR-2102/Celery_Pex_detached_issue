# celery_example
Example of packaging Celery with PEX. 

This demonstrates headless/detached celery worker running issue.


# To Build PEX file

Clone repo.

Run 'make clean build'.

Pex file will be created in ./dist sub dir.

(dist dir and .pex has also been included here).


# To run Celery from the PEX

- Start Celery beat:

PEX_SCRIPT=celery ./dist/example.celery.pex beat --app=app.worker.app --loglevel=DEBUG --logfile=./celeryBeat.log

- Start Celery worker:

PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --loglevel=DEBUG --logfile=./celeryWorker.log


# Celery headless issue demonstration

- Running the beat detached:

	PEX_SCRIPT=celery ./dist/example.celery.pex beat --app=app.worker.app --detach --loglevel=DEBUG --logfile=./celeryBeatDetach.log

The beat starts and runs as expected.

- Running the worker detached:

To see more run information, set the environmental variable PEX_VERBOSE to 5:

export PEX_VERBOSE=5

Attempt to start the Celery worker headless:

	PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --detach --loglevel=DEBUG --logfile=./celeryWorkerDetach.log

The last line of output as it errors should look something like:

pex:     ~/.pex/install/amqp-2.4.2-py2.py3-none-any.whl.0947f8676094f8ddeaff8e64f7e11729b544df03/amqp-2.4.2-py2.py3-none-any.whl
pex:   * ~/python_work/celery_example/dist/example.celery.pex/.bootstrap
pex:   * - paths that do not exist or will be imported via zipimport
In app.worker.py

This isn't particularly helpful and after digging into the code it can be seen at some point the stdout and error out are redirected to null and the process is forked.

Commenting the redirection out displays more info on what is happening, to do this go to the pex cache dir and find the celery files which are being run, in this case:

	~/.pex/install/celery-4.2.1-py2.py3-none-any.whl.79938b815d642fb6adfd6178bdd22f2f94a24a66/celery-4.2.1-py2.py3-none-any.whl/celery

Open platforms.py and update the method redirect_to_null nested within class DaemonContext(object) to:

    def redirect_to_null(self, fd):
        print(100*"X")
        pass
        #if fd is not None:
        #    dest = os.open(os.devnull, os.O_RDWR)
        #    os.dup2(dest, fd)

This will show more info on the std out.

Running the start command again:

	PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --detach --loglevel=DEBUG --logfile=./celeryWorkerDetach.log

The last line of the output is now:

	/usr/local/opt/python/bin/python3.7: No module named celery

Note - if you have celery in your default Python environment then it will not fail and you will not see the error.

The issue looks to me as though the detached process is launched outside of the pex environment and so can't find the required Celery package.

This might sound reasonable but I do not understand why the Celery beat works in detached mode.

My questions are:

	Is there a work around to be able to launch a detached Celery worker from a Pex file?

	Why does this work for the Celery beat but not the worker?

