.PHONY: test build

test:
\tpytest -q

build:
\tpython -m src.supernova.train
