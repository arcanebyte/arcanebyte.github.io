# One Hugo site on themes/base.
#   make dev          arcanebyte on :1313
#   make build        into dist/
#   make docker       build and run the nginx image
#   make check        build and look for broken links and missing images

HUGO ?= hugo

.PHONY: dev product build clean docker docker-build check help

help:
	@grep -E '^[a-z-]+:.*?##' $(MAKEFILE_LIST) | sed 's/:.*##/\t/' | column -t -s "$$(printf '\t')"

dev: ## Serve arcanebyte.com on :1313
	$(HUGO) server --source sites/arcanebyte --port 1313 --bind 127.0.0.1

product: ## New product page: make product name=widget2lisa
	@test -n "$(name)" || { echo "usage: make product name=widget2lisa"; exit 1; }
	$(HUGO) new content --source sites/arcanebyte products/$(name).md
	mkdir -p sites/arcanebyte/assets/img/products/$(name)

build: ## Build the site into dist/
	$(HUGO) --source sites/arcanebyte --minify --cleanDestinationDir \
	  --destination ../../dist/arcanebyte

check: build ## Build, then check links and images
	@python3 scripts/check_output.py dist/arcanebyte

docker-build: ## Build the nginx image
	docker build -t arcanebyte-sites -f deploy/Dockerfile .

docker: ## Build and run the site in Docker
	docker compose up --build

clean:
	rm -rf dist sites/*/public sites/*/resources
