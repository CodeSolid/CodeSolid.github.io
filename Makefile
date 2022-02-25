phony: book build labkill lab wc
book: build
	open file:///Users/johnlockwood/source/CodeSolid/CodeSolid.github.io/booksource/_build/html/index.html 

build:
	jupyter-book build booksource

lab:
	@jupyter lab booksource > /dev/null &
	@echo "Running Jupyter Lab..."

.ONESHELL:
labkill:
	kill ```ps aux | grep jupyter-lab | awk 'NR==1{print $2}'```
	echo done

wc:
	cat booksource/* | wc -w