# Edge-Detection-Comparision
###Modules needed to be pre-installed
* scipy
* numpy
* matplotlib

###Command Line Execution
* Single thread version

  `python edgeDetection_single.py  -i [input image file]  -o [output image file]`

* Multiple thread version

  `python edgeDetection_multiple.py  -i [input image file]  -o [output image file]  -t [thread number]`

Output file and thread number is optional.

The default value for them is 'output.png' and multiprocessing.cpu_count()*2.

###Concurrency Performance Evaluation
* Single thread version

  `python test_single.py  -i [input image file]  -o [output image file] -n [number of repetitive execution]`

* Multiple thread version

  `python test_multiple.py  -i [input image file]  -o [output image file]  -t [thread number] -n [number of repetitive execution]`
