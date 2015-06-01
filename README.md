# Edge-Detection-Comparision
###Modules needed to be pre-installed
* scipy
* numpy

###Command Line Execution
* Single thread version

  `python edgeDetection_single.py  -i [input image file]  -o [output image file]`

* Multiple thread version

  `python edgeDetection_Multiple.py  -i [input image file]  -o [output image file]  -t [thread number]`

Output file and thread number is optional.

The default value for them is 'output.png' and multiprocessing.cpu_count()*2.
