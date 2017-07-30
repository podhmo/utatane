%.png: %.py
	python $< dump $@

default: $(shell ls *.py | sed 's@\.py$$@.png@g;') readme

readme:
	python -c 'import glob; import json; print(json.dumps({"files": sorted(glob.glob("*plot_*.py"))}))' | kamidana -a kamidana.additionals.reader -i json misc/gallery.jinja2 > readme.md

clean: $(shell ls *.png)
	rm -f $^
