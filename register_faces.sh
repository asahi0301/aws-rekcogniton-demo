#for i in `find . -type f | grep jpeg | grep index |cut -c 3-`; do echo $i ; done
for i in `find . -type f | grep jpeg | grep index |cut -c 3-`; do python index_faces.py $i ; done
for i in `find . -type f | grep jpg | grep index |cut -c 3-`; do python index_faces.py $i ; done
for i in `find . -type f | grep png | grep index |cut -c 3-`; do python index_faces.py $i ; done