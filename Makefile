build:
	@docker build -t pyspark .

start:
	@docker run \
		--name pyspark \
		-d \
		-e JUPYTER_ENABLE_LAB=yes \
		-p 8888:8888 \
		-v $(PWD):/home/jovyan \
		pyspark

stop:
	@docker stop pyspark
	@docker rm pyspark

logs:
	@docker logs pyspark

run:
	@docker exec -it pyspark python3 src/main.py

test: test-pytest test-pylint

test-pytest:
	@echo "Runnning pytest..."
	@docker run --rm -v $(PWD):/home/jovyan pyspark pytest

test-pylint:
	@echo "Running pylint..."
	@docker run --rm -v $(PWD):/src wpengine/pylint:python-3.7 /src
