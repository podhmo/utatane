%.svg: %.py
	python $< dump $@

default: $(shell ls *.py | sed 's@\.py$$@.svg@g;')

clean: $(shell ls *.svg)
	rm -f $^
