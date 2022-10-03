docker-build:
	docker build -t videotranslate .

docker-run:
	docker run -d -p 8501:8501 videotranslate


start:
	make docker-build 
	make docker-run 