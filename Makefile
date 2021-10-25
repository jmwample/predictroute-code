
# IMAGE_NAME=predict-route
IMAGE_NAME=graph-tool-testing

all:
	docker build -t ${IMAGE_NAME} -f docker/Dockerfile .

run:
	docker run -it --rm --name ${IMAGE_NAME}-run ${IMAGE_NAME}

test:
	docker build -t conda-test --target test -f docker/Dockerfile .

test-run:
	docker run -it --rm --name conda-test-run conda-test
