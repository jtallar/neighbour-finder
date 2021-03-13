# Simulacion de Sistemas
## Trabajo Practico N°1
### "Busqueda Eficiente de Particulas Vecinas"
First simulation of static particles distance applying Cell Index Method

## What to Install
python -m pip install numpy         # TODO: Change to generic command

## Previous filename configuration
filenameConfig.json contains the names of all the files generated and used throughout the simulation
They can only be modified before first execution

## Generate random particles --> dynamic and static files
`python generator.py N L`

Where 
- `N` is the number of particles to simulate
- `L` is the side lenght

Eg: `python generator.py 150 100`

## Apply Cell Index Method on recently generated particles
`python cim.py Rc (periodic|not_periodic) [M]`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)
- `[M]` is an optional parameter to specify block side count

Eg: `python cim.py 50 periodic 2`

## Obtain every pair of particle distance by brute force
`python bruteForce.py Rc (periodic|not_periodic)`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)

Eg: `python bruteForce.py 50 periodic`

## Originate OVITO input file to simulate results
`python ovito.py id`

Where 
- `id` is the particle number that wants to be studied

Eg: `python ovito.py 32`


## Extra Material
### In plots folder, all the execution times of the simulations under different conditions specified in each case