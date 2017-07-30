%.png: %.py
	python $< dump $@

default: $(shell ls *.py | sed 's@\.py$$@.png@g;')

clean: $(shell ls *.png)
	rm -f $^
