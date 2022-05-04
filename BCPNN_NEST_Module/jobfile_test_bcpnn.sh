#!/bin/bash -l


#SBATCH -A project_name_allocation
#SBATCH -J bcpnn_test_job

# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 0:59:00

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32

#SBATCH -e error_file.e
#SBATCH -o output_file.o



module swap PrgEnv-cray PrgEnv-gnu
module add nest/2.2.2-conda-py27 #formerly just module add nest, but this seems to load the wrong version now?
module add mpi4py/3.0.2/py27
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/cfs/klemming/nobackup/usr/Beskow_BCPNN/build-module-100725  # usr-> u/usr


# Run and write the output into my_output_file
aprun -n 2 python test_installation_beskow.py > delme_test_installation 2>&1
echo "Stopping test 1 at `date`"

echo "Starting test 2 at `date`"
aprun -n 2 python test.py > delme_test_connect 2>&1
echo "Stopping test 2 at `date`"
