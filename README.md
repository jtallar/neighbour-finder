# Simulacion de Sistemas
## Trabajo Practico N°1: "Busqueda Eficiente de Particulas Vecinas"
### First simulation of static particles distance applying Cell Index Method

## What to Install
- `python3 -m pip install numpy`
- Download and install OVITO from: https://www.ovito.org/
### Versions
`python 3.8`

## 0. Previous filename configuration
`filenameConfig.json` contains the names of all the files generated and used throughout the simulation.
They can only be modified before first execution.

## 1. Generate random particles (CIM input files)
`python3 generator.py N L [rp]`

Where 
- `N` is the number of particles to simulate
- `L` is the side lenght
- `[rp]` is an optional parameter to specify every particle radius. If not specified, each particle will have a random value from 0 to 1.

Eg: `python3 generator.py 500 20 0.25`

### Output
Generates files with static data (default name: `static.txt`) and dynamic data (default name: `dynamic.txt`)

## 2. Apply Cell Index Method on recently generated particles to obtain list of neighbours
`python3 cim.py Rc (periodic|not_periodic) [M]`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)
- `[M]` is an optional parameter to specify block side count. If not specified, optimal M value will be used.

Eg: `python3 cim.py 1 periodic 2`

### Input
Files with static and dynamic data

### Output
Generates file (default name: `out.txt`) where each line represents a particle and has each particle id followed by its neighbours.

Line example: 500->107,474,499,206

## 2. ALTERNATIVE: Apply brute force to obtain list of neighbours
`python3 bruteForce.py Rc (periodic|not_periodic)`

Where 
- `Rc` is the radio of interaction to study
- `periodic|not_periodic` is the edge periodic condition (periodic or not)

Eg: `python3 bruteForce.py 1 periodic`

### Input
Files with static and dynamic data

### Output
Generates file (default name: `out.txt`) where each line represents a particle and has each particle id followed by its neighbours.

Line example: 500->107,474,499,206

## 3. Originate OVITO '.xyz' input file to simulate results
`python3 ovito.py id`

Where 
- `id` is the particle number that wants to be studied

Eg: `python3 ovito.py 32`

### Input
Files with static and dynamic data, and list of neighbours file

### Output
Generates file (default name: `simulation.xyz`) with simulation figure.

## 4. Open '.xyz' with Ovito
To view the simulation figure, follow this steps:
1. Run Ovito.
2. Load the `.xyz` file previously generated. You can run and load the file with `./bin/ovito simulation.xyz` or run Ovito and then use Load File option.
3. Configure the file column mapping as follows
    - Column 1 - Radius
    - Column 2 - Position - X
    - Column 3 - Position - Y
    - Column 4 - Particle Identifier
    - Column 5 - Color - R
    - Column 6 - Color - G
    - Column 7 - Color - B

Once the figure shows, you can Render Active Viewport, where you can save it as a `.png` file.

### Extra Material
In `plots` folder, all the execution times of the simulations under different conditions specified in each case.
