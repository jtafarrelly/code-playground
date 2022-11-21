#
# mpi4py implementation of the 2D Ising Model
#
# Run by typing:
# mpiexec -np <THREAD_NUM> python mpi_IsingModel.py
#

import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt
import sys
import csv


def plot_image(data,file_name):
    plt.figure()
    plt.set_cmap('hot')
    plt.imshow(data)
    plt.savefig(file_name)

#Physical parameters - USAGE: mpiexec -np <NUM_THREADS> mpi_Ising_Model.py <LATTICE DIMENSIONS> <ITERATIONS> <FLIPS PER ITERATION>



dimensions = int(sys.argv[1])
num_iteration = int(sys.argv[2])
flips_per_iteration = int(sys.argv[3])
exchange_constant = -1
KbT = 1.3806E-23 * 5

energy_cost = np.empty(2)

energy_cost[0] = np.exp(4 * (exchange_constant / KbT))
energy_cost[1] = energy_cost[0] ** 2 #Only two possible energy costs for a flip - do not need to calculate each time!

lattice_edgestates = np.empty((dimensions, 2))

#MPI message tags.

master_ID = 0

START_TAG = 1

TOP_TAG = 2
BOTTOM_TAG = 3

FINISH_TAG = 4

SENDING_BOTTOM = 11
SENDING_TOP = 12

UPDATE_BOTTOM_EDGE = False
UPDATE_TOP_EDGE = False

#MPI Parameters

comm_group = MPI.COMM_WORLD

num_threads = comm_group.Get_size() - 1 #excluding the master process
process_ID = comm_group.Get_rank()

lattice_edgestates = np.empty((dimensions, 2))


print(sys.argv)

if process_ID == master_ID: 
    
    #Initialising environment

    print("Enter the parameters of the lattice and metropolis algorithm:")
    print("Format: <LATTICE DIMENSIONS> <ITERATION NUMBER> <SPIN FLIPS PER ITERATION>")

    print("Initialising lattice of dimension {}.".format(dimensions))
    sys.stdout.flush()

    init_lattice = np.random.choice([-1,1], (dimensions, dimensions))
    init_lattice = init_lattice.astype(np.intc)

    start_time = MPI.Wtime()

    sublattice_blocks = np.array_split(init_lattice, num_threads) #divide initial lattice into appropriate row-ordered subgroups

    for i in range(1,num_threads+1):

        #telling processes what the neightbouring threads are, enforcing top-bottom periodic boundary conditions
        if i == 1: 
            top = num_threads
        else:
            top = i - 1

        if i == num_threads:
            bottom = 1
        else:
            bottom = i + 1

        #send out the appropriate sublattice blocks and neighbours to the worker threads

        comm_group.send(sublattice_blocks[i-1], dest = i, tag = START_TAG)
        comm_group.send(top, dest = i, tag = START_TAG)
        comm_group.send(bottom, dest = i, tag = START_TAG)
        

    
    # Recieve the iterated sublattices from threads

    for i in range(1,num_threads+1):

        lattice_request = comm_group.recv(source = i, tag = FINISH_TAG)
        
        sublattice_blocks[i-1] = lattice_request
        print("Master thread recieved sublattice %i" % i)

    finish_time = MPI.Wtime()

    MPI.Finalize()

    print("exited loop, concatenating")

    file_name = 'mpi_runtime_%ix%i.csv' % (dimensions, dimensions)

    file = open(file_name, 'a+', newline='')
    writer = csv.writer(file)
    writer.writerow([num_threads, finish_time-start_time])

    # Rejoin the sublattices into the full lattice

    fin_lattice = np.concatenate(sublattice_blocks)








elif process_ID != master_ID:

# Recieve neighbours and sublattice from master thread

    sublattice = comm_group.recv(source = master_ID, tag=START_TAG)
    top = comm_group.recv(source = master_ID, tag = START_TAG)
    bottom = comm_group.recv(source = master_ID, tag = START_TAG)

    #get the dimensions of the sublattice, numpy is by default row-ordered ie. [i,j] = [y, x]

    print(sublattice.shape)

    y_max = sublattice.shape[0] - 1
    x_max = sublattice.shape[1] - 1

    top_storage = np.empty(x_max, dtype=np.intc)
    bottom_storage = np.empty(y_max, dtype=np.intc)

    #broadcast the initial edge states to the neighbouring threads


    print("Process %i: My neighbours are processes %i and %i." % (process_ID, top, bottom))
    sys.stdout.flush()

    comm_group.send(sublattice[0], dest=top,tag = SENDING_TOP)
    bottom_buffer = comm_group.recv(source = bottom, tag = SENDING_TOP)


    comm_group.send(sublattice[y_max], dest=bottom,tag = SENDING_BOTTOM)
    top_buffer = comm_group.recv(source = top, tag = SENDING_BOTTOM)



    #recieve edge states from neighbouring threads

    #Blocking to sychronise all threads.

    print("Sent and recieved on process %i" % process_ID)
    sys.stdout.flush()

    #Main metropolis loop

    print("Process %i beginning lattice iterations." % process_ID)
    sys.stdout.flush()

    BOTTOM_STORAGE_FULL = False
    TOP_STORAGE_FULL = False
    # top_request = MPI.Request
    # bottom_request = MPI.Request

    for iterations in range(num_iteration):

        #print("Iteration %i on Process %i" % (iterations, process_ID))

        rng_vals = np.random.uniform(size =(3, flips_per_iteration))

        for flips in range(flips_per_iteration):
        
            #Initiate a request for the neighbouring edge states if there is no active request currently - do not want to reuse buffer that is already active
            
            if TOP_STORAGE_FULL == False:

                #print("Process %i requesting top data." % process_ID)

                top_request = comm_group.irecv(source = top, tag = SENDING_BOTTOM) #requesting the bottom edge states of block above
                TOP_STORAGE_FULL = True
                

            if BOTTOM_STORAGE_FULL == False:

                #print("Process %i requesting bottom data." % process_ID)
                bottom_request = comm_group.irecv(source = bottom, tag = SENDING_TOP) #requesting the top edge states of block below
                BOTTOM_STORAGE_FULL = True

            # Checking if a message has been recieved from the neighbours, updating the buffer if so.

            top_storage = top_request.test()
            bottom_storage = bottom_request.test()

            if top_storage[0] == True:
                top_buffer = top_storage[1]
                #print("Process %i recieved top data." % process_ID)
                TOP_STORAGE_FULL = False

            if bottom_storage[0] == True:
                bottom_buffer = bottom_storage[1]
                #print("Process %i recieved bottom data." % process_ID)
                BOTTOM_STORAGE_FULL = False


            #generating a random coordinate within the sublattice

            i = int(rng_vals[0,flips] * y_max + 0.5)
            j = int(rng_vals[1,flips] * x_max + 0.5)



            #if random y coord is on the boundary, pull the appropriate value from the buffer

            if i == y_max:
                top_val = sublattice[i-1,j]
                bottom_val = bottom_buffer[j]

                UPDATE_BOTTOM_EDGE = True #Signalling that the edge may be updated and a message may need to be passed to the appropriate neighbour
                UPDATE_TOP_EDGE = False 

            elif i == 0:
                top_val = top_buffer[j]
                bottom_val = sublattice[i+1,j]

                UPDATE_TOP_EDGE = True
                UPDATE_BOTTOM_EDGE = False
            else:
                top_val = sublattice[i-1,j]
                bottom_val = sublattice[i+1,j]

                UPDATE_BOTTOM_EDGE = False
                UPDATE_TOP_EDGE = False

            #Determining the values of the nearest neighbours; enforcing horizontal periodic boundary conditions

            if j == x_max:
                left_val = sublattice[i,j-1]
                right_val = sublattice[i,0]
            elif j == 0:
                left_val = sublattice[i,x_max]
                right_val = sublattice[i,j+1]
            else:
                left_val = sublattice[i,j-1]
                right_val = sublattice[i,j+1]
            

            lattice_sum = sublattice[i,j] * ( left_val + right_val + top_val + bottom_val)

            if lattice_sum <= 0 or rng_vals[2,flips] < energy_cost[(lattice_sum // 4) - 1]:

                sublattice[i,j] *= -1 #flip the spin!

                #if the spin is flipped on the boundary, send the updated boundary states to the neighbour

                if UPDATE_TOP_EDGE == True:
                    
                    #print("Process %i sending top data to %i" % (process_ID,top))
                    #print([i,j])
                    comm_group.send(sublattice[0],dest = top, tag = SENDING_TOP)
                    UPDATE_TOP_EDGE == False


                elif UPDATE_BOTTOM_EDGE == True:
                    
                    #print("Process %i sending bottom data to %i" % (process_ID,bottom))
                    #print([i,j])
                    comm_group.send(sublattice[y_max],dest = bottom, tag = SENDING_BOTTOM)
                    UPDATE_BOTTOM_EDGE == False
            else:
                pass

    # Send fully iterated sublattice back to the master thread

    comm_group.send(sublattice, dest = master_ID, tag = FINISH_TAG)

    MPI.Finalize()



            

            



    

#Message passing between neighbouring threads/lattice blocks

