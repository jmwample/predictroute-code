
# IMAGE_NAME=predict-route
IMAGE_NAME=graph-tool-testing

all:
	docker build -t ${IMAGE_NAME} -f docker/Dockerfile .

run:
	docker run -it --rm --name ${IMAGE_NAME}-run ${IMAGE_NAME}
