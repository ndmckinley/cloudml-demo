.PHONY: local
local: redis-local webapp-local worker-local

.PHONY: all
all: redis webapp worker

.PHONY: delete
delete: delete-redis delete-webapp delete-worker

.PHONY: redis
redis:
	$(MAKE) -C redis all

.PHONY: webapp
webapp:
	$(MAKE) -C webapp all

.PHONY: worker
worker:
	$(MAKE) -C worker all

.PHONY: redis-local
redis-local:
	$(MAKE) -C redis local

.PHONY: webapp-local
webapp-local:
	$(MAKE) -C webapp local

.PHONY: worker-local
worker:
	$(MAKE) -C worker local

.PHONY: delete-redis
delete-redis:
	$(MAKE) -C redis delete

.PHONY: delete-webapp
delete-webapp:
	$(MAKE) -C webapp delete

.PHONY: delete-worker
delete-worker:
	$(MAKE) -C worker delete
