![build](https://github.com/marcelrienks/gameOfLife/workflows/build/badge.svg)

# gameOfLife
Simple console app to test Conway's game of life, using mutiple 2 dimentional arrays to keep track of, and calculate the next life cycle of live and dead cells. Possibly not the most resource efficient way to handle this, but the most logical, at least for me.

## How to use it
From a command prompt in the root directory, type the following to launch the app, and follow the instructions to run.  
`python gameOfLife.py`

## Grid Size and seed
The grid size input is the horizontal, and vertical size, followed by the seed in the following format `0x0:0`.  
_i.e._ a size of 10 horizontally, and 5 vertially, with a seed of 27, will look as follows  
`10x5:27`
