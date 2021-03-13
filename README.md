# Simulacion de Sistemas
## Trabajo Practico N°1: "Busqueda Eficiente de Particulas Vecinas"
### First simulation of static particles distance applying Cell Index Method

## What to Install
`python3 -m pip install numpy`
### Versions
`python 3.8`

## Previous filename configuration
`filenameConfig.json` contains the names of all the files generated and used throughout the simulation.
They can only be modified before first execution.

## Generate random particles (CIM input files)
- `python3 generator.py N L`
- `pip3 install -U ovito`
- Download and install OVITO from: https://www.ovito.org/

Where 
- `N` is the number of particles to simulate
- `L` is the side lenght

Eg: `python3 generator.py 150 100`

## Apply Cell Index Method on recently generated particles
`python3 cim.py Rc (periodic|not_periodic) [M]`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)
- `[M]` is an optional parameter to specify block side count

Eg: `python3 cim.py 50 periodic 2`

## Obtain every pair of particle distance by brute force
`python3 bruteForce.py Rc (periodic|not_periodic)`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)

Eg: `python3 bruteForce.py 50 periodic`

## Originate OVITO '.xyz' input file to simulate results
`python3 ovito.py id`

Where 
- `id` is the particle number that wants to be studied

Eg: `python3 ovito.py 32`


### Extra Material
In `plots` folder, all the execution times of the simulations under different conditions specified in each case
