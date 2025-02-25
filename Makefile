build-and-push:
	docker build -t registry.baselinehq.cloud:5001/costgraph-superset:v1 .
	docker push registry.baselinehq.cloud:5001/costgraph-superset:v1