download:
	@wget -P data/raw https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv

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
	@docker exec -it pyspark python3 src/main.py $(pipeline)

test: test-pytest test-pylint

test-pytest:
	@echo "Runnning pytest..."
	@docker run \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-v $(PWD):/home/jovyan \
		pyspark python -m pytest --disable-pytest-warnings

test-pylint:
	@echo "Running pylint..."
	@docker run \
		--rm \
		-v $(PWD):/src \
		wpengine/pylint:python-3.7 /src --rcfile=/src/.pylintrc
