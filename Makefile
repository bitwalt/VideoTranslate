build:
	docker-compose build --no-cache 

up:
	docker-compose up -d  

down:
	docker-compose down  

start:
	make build 
	make up  

stop:
	make down  
