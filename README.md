# hoomd-install
Issue: hoomd after version 2.3 (with cuda 8.0) can't be naively installed with conda and running with cuda. If one installed by conda, it will only run with cpus.

Target: Installing hoomd and running with Nvidia gpu under ubuntu 18.04 in local dekstop (sudo required), not sure how to do without sudo or in cluster yet.

Prerequisites: working conda and cuda

Prerequisites  libraries:
     
    conda install -c conda-forge sphinx git openmpi numpy cmake

Install hoomd first:

    conda install -c conda-forge hoomd
    conda update hoomd
     
compile: 
(change /usr to the folder contain /lib/python3)
(cd to your favorite location)

    export SOFTWARE_ROOT=/usr
    git clone --recursive https://bitbucket.org/glotzer/hoomd-blue
    cd hoomd-blue
    mkdir build
    cd build
    cmake ../ -DCMAKE_INSTALL_PREFIX=${SOFTWARE_ROOT}/lib/python3
    
for cuda 

    cmake ../ -DCMAKE_INSTALL_PREFIX=${SOFTWARE_ROOT}/lib/python3 -DCMAKE_CXX_FLAGS=-march=native -DCMAKE_C_FLAGS=-march=native -DENABLE_CUDA=ON
      
for cuda+MPI
 
    cmake ../ -DCMAKE_INSTALL_PREFIX=${SOFTWARE_ROOT}/lib/python3 -DCMAKE_CXX_FLAGS=-march=native -DCMAKE_C_FLAGS=-march=native -DENABLE_CUDA=ON -DENABLE_MPI=ON


pre-test

    make -j4
    ctest
    
if not all passed, something wrong. If all passed, then install by

    sudo make install 
    export PYTHONPATH=$PYTHONPATH:${SOFTWARE_ROOT}/lib/python3
      

test (test.py is provided):

    python3 test.py --gpu=0

(change number to desired gpu, run "nvidia-smi" to check)
     

if it work, write 

    export PYTHONPATH=$PYTHONPATH:/usr/lib/python3
     
in your ~/.bashrc, or just run this line every time, as you like.
Good luck
