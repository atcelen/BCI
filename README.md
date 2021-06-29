
Authors: Ata Celen, Boran Deniz Yaralioglu

# Motor Imagery Brain–Computer Interfaces: Dataset Acquisition and System Evaluation

In this repository, we share the code for classifying MM data using a custom created dataset using a ModularBCI board. This repository only caries the code for the training of the neural network model(main_global.py), the real-time prediction inteface Python script(predictor.py), the computer-robot interface Python script(Navigating Nao/Navigating Nao.sln) and the PyschoPy experiment script(FirstExperiment.py).



#### Installing Dependencies
You will need a machine with a CUDA-enabled GPU and the Nvidia SDK installed to compile the CUDA kernels.
Further, we have used conda as a python package manager and exported the environment specifications to `dependency.yml`. 
You can recreate our environment by running 

```
conda env create -f dependency.yml -n mybciEnv 
```
Make sure to activate the environment before running any code. 

If get a batchnormalization error when running the code, follow the instructions by gurjar112 [here](https://github.com/keras-team/keras/issues/10648): 

change "()" to "[ ]" in line no 1908,1910,1914, 1918 in anaconda3/envs/mybciEnv/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py (e.g. beta = tf.reshape(beta, [-1])) and have 'channels_last' in keras.json


#### Training and Validation
Global models are trained and validated in `main_global.py`. Results are in `results/your-global-experiment/stats` and global models in `results/your-experiment-name/model`. 
```
$ (mybciEnv) python3 main_global.py

```
#### Running the Experiment
After downloading the "PsychoPy Runner" software from PsychoPy's website, the "FirstExperiment.py" is run inside this software. Before running the code, the IP address from the computer that runs the Acquisition Server for the ModularBCI board has to be taken and inserted inside the code.

#### Running the predictor
Before running the predictor script, it has to be made sure that the "LSL Export" box inside OpenViBE Designer is used.
```
$ (mybciEnv) python3 predictor.py

```
#### Running the Computer-Robot Interface Script
The "predictor.py" script has to be run first so that the navigation script can get the prediction using the sockets. It is important to note that both scripts have to communicate over the same port. Also, Python 2.7 has to installed and the PYTHONPATH for the naoqi library has to be added to run this script.   
  


### License and Attribution
In our project we have heavily used the training and validation methods from the paper :
Xiaying Wang, Michael Hersche, Batuhan Tömekce, Burak Kaya, Michele Magno, Luca Benini, "An Accurate EEGNet-based Motor-Imagery Brain--Computer Interface for Low-Power Edge Computing", in IEEE International Symposium on Medical Measurements and Applications (MEMEA), 2020.
https://github.com/MHersche/eegnet-based-embedded-bci 

