default: gen
	python plot.py dump without-fixture.png
	python plot.py --data data.json dump with-fixture.png

gen:
	python gen.py > data.json

without-fixture:
	python plot.py

with-fixture:
	python plot.py --data data.json
