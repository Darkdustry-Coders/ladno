#!/bin/sh

# A simple shell script to add headers (like copyright statements) in files
# from https://github.com/miguelgfierro/scripts/

for f in $1; do
	echo Processing $f
	cat header $f > $f.new
	mv $f.new $f
done
echo Process finished  
