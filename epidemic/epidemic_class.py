import numpy as np
import sympy as syp
from pprint import pprint
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
#
#  The epidemic class
#
class epidemic():
    """  This class handles all of the operations for an epidemic model

    """
    #
    def __init__(self,max_time_steps = None, dim = 2, d = None,
    target_size = None, 
    prob_recover = None, prob_local_infect = None,
    prob_long_dist_infect = None,
    ):
        assert d is not None
        assert isinstance(dim, int)
        assert dim == 2  #Right now this is only a 2D model
        assert target_size is not None
        assert self._check_prob_(prob_recover)
        assert self._check_prob_(prob_local_infect)
        assert self._check_prob_(prob_long_dist_infect)
        #
        #  Define the initialization state
        #
        self.S = np.int(0)  #susceptible state
        self.I = np.int(1)  #infected state
        self.R = np.int(2)  #recovered state
        self.current_time = 0
        self.max_time = int(max_time_steps)
        self.VERBOSE = False
        self.max_time_steps = 200  #The maximum time steps
        self.dim = 2  #The number of dimensions to use
        self.d = -1.0 #This is a place holder
        self.coord_list = None
        #  The next three describe the population
        self.pop_size = None
        self.edge_size = None
        self.people_state = None
        #  These are the state transition probabilities
        self.prob_recover = prob_recover
        self.prob_local_infect = prob_local_infect
        self.prob_long_dist_infect = prob_long_dist_infect
        #
        self.max_time_steps = max_time_steps if (not (max_time_steps is None)) else 200
        self.d = d
        #build the coordinate list
        self.coord_list = self._generate_coordinate_list_(self.dim, self.d)
        #build the initial state
        self.pop_size, self.edge_size, self.people_state = self.create_population_(self.dim, target_size)
    ######################################################
    #  The public functions that are accessors for the public
    ######################################################
    def get_coordinate_list(self):
        return self.coord_list
    def get_people_state(self):
        return self.people_state
    def get_population_size(self):
        return self.pop_size
    def get_edge_size(self):
        return self.edge_size
    def get_prob_recovery(self):
        return self.prob_recover
    def get_prob_local_infect(self):
        return self.prob_local_infect
    def get_prob_long_dist_infect(self):
        return self.prob_long_dist_infect
    def get_number_recovered(self):
        return len(np.where(self.person_state == self.R)[0])
    def get_number_infected(self):
        return len(np.where(self.person_state == self.I)[0])
    def get_number_susceptible(self):
        return len(np.where(self.person_state == self.S)[0])
    def get_verbose(self):
        return self.VERBOSE
    #####################################################
    #  Public setter functions
    #####################################################
    def toggle_verbose(self):
        self.VERBOSE = not self.VERBOSE
    def set_verbose(self, inVal = None):
        if inVal is None:
            self.toggle_verbose()
        else:
            self.VERBOSE = inVal
    #####################################################
    #  Public action functions
    #####################################################
    #
    #  Define a function for a single time step
    #
    def single_time_step(self):
        self._single_time_step_()
    ######################################################
    #  The private functions that will only be called internally
    ######################################################  
    #
    #  simple range checker for probabilities
    #
    def _check_prob_(self, in_val = None):
        if in_val is None:
            return False
        if not isinstance(in_val,np.float64):
            in_val = np.float64(in_val)
        if in_val < 0.0:
            return False
        if in_val > 1.0:
            return False
        return True
    def _single_time_step_(self):
        # print(i_state)
        if self.VERBOSE:
            print("Current Time: {}".format(self.current_time))
        infected_persons = np.where(self.person_state == self.I)
        num_infected = len(infected_persons[0])
        # print(num_infected)
        rand_to_recover = np.random.uniform(size=num_infected)
        recovered = np.where(rand_to_recover < self.prob_recover)
        recovered_indices = tuple([infected_persons[i][recovered] for i in range(self.dim)])
        for c in close_indices:
            c_indices = [self._wrap_(self.edge_size,infected_persons[i] + c[i]) for i in range(self.dim)]
            infected_indices = self._choose_random_indices_(c_indices, self.prob_local_infect)
            if len(infected_indices) > 0:
                s_state_indices = np.where(self.person_state[infected_indices] == self.S)
                new_infections_indices = tuple([infected_indices[i][s_state_indices] for i in range(self.dim)])
                self.person_state[new_infections_indices] = self.I
        #Try long distance infections
        rand_long_indices = np.random.randint(edge_size,size=(num_infected,self.dim))
        rand_choose = np.where(np.random.uniform(size = num_infected) < self.prob_long_dist_infect)
        rand_long_indices = rand_long_indices[rand_choose]
        if len(rand_choose) > 0:
            parallel_indices = tuple([rand_long_indices[:,i] for i in range(self.dim)])
            s_state_indices = np.where(self.person_state[parallel_indices] ==  self.S)
            s_state_indices = s_state_indices[0]
            if len(s_state_indices) > 0:
                update_indices = tuple([rand_long_indices[:,i][s_state_indices] for i in range(lattice_dim)])
                person_state[update_indices] = self.I
        person_state[recovered_indices] =  self.R
    #
    #  Create Population  -  We always create a population with the approximate size
    #
    def _create_population_(self, n_dim = None, total_pop = None):
        """  Creates the city population and initialize to the s_state

        Inputs:
            n_dim - number of dimensions of the lattice
            total_pop - Approximate number of people

        Outputs:
            computed_pop - computed number of people to use
            edge_size - The length of each edge in the lattice
            pop_lattice - the state lattice
        """
        lattice_dim = np.int(n_dim)
        edge_size = np.int(np.float64(N)**(1./lattice_dim) + .5)
        computed_pop = edge_size ** lattice_dim
        lattice_struct = tuple([edge_size for i in range(lattice_dim)])
        pop_lattice = np.zeros(lattice_struct).astype(int)  
        pop_lattice.fill(self.S)
        return computed_pop, edge_size, pop_lattice  
    #
    #  Generate the list of coordinates within d distance - We always create a coordinate list
    #
    def _generate_coordinate_list_(self, dim = None, dist = None):
        '''  This generates the list of integer coordinates around 0,0 within a given euclidean distance
            NOTE:  This uses a recursive algorithm

        Input:
            dim - The number of dimensions to use
            dist - the distance to use

        Output:
            A python list of the valid interger coordinates within the given euclidean distance
            NOTE:  These are centered on the origin, so they need to be added to the coordinates use
            in the computations.
        '''
        assert dim is not None
        assert isinstance(dim, int)
        assert dim >= 1
        assert dim <= 3
        assert dist is not None
        assert isinstance(dist,np.float64)
        assert dist >= 1.0
        assert dist <= 5.0

        if dim == 1:
            n_dist = int(dist)
            list_index = [[i] for i in range(-n_dist, n_dist + 1,1)]
            return =  list_index
        else:
            n_dist = int(dist)
            lower_list = generate_coordinate_list(dim - 1, dist)
            t_list = [ l + [i] for l in lower_list for i in range(-n_dist, n_dist + 1,1)]
            list_index = [l for l in t_list if np.linalg.norm(np.array(l)) <= dist]
            return  list_index
    #
    #  The wrap function
    #
    def _wrap_(max_val = None, indices = None):
        """  This wraps the values so there are no negative indices or huge indices
            NOTE:  This is the helper function that hides the multiple indices

        Input:
            max_val : an integer for the lengthe of the mesh used in epidemic studies
                NOTE:  Assumes that each dimension is the same
                NOTE:  Assumes that 0 is always the lowest value
            indices :  The indices to check  (as an numpy array)
                NOTE:  These must have the same lengths

        Output:
            A copy of the indices with the torus wrapped values
        """
        assert max_val is not None
        assert max_val > 0
        assert indices is not None
        assert isinstance(indices,np.ndarray)
        #
        w_indices = np.copy(indices)
        large_indices = np.where(w_indices >= max_val)
        w_indices[large_indices] = w_indices[large_indices] - max_val
        small_indices = np.where(w_indices < 0)
        w_indices[small_indices] = max_val + w_indices[small_indices]
        return w_indices
    #
    #  Choose random subset of indices
    #
    def _choose_random_indices_(self, indices = None, q = None):
        '''Choose a random subset of indices based upon 

        Input:
            indices - The indices to choose
            q - The value to compare the random number against for choice

        Output:
            work_indices - An appropriate subset of indices
        '''
        assert indices is not None
        assert len(indices) > 0
        assert q is not None
        assert isinstance(q, np.float64)
        assert q >= 0.0
        assert q <= 1.0
        num_indices = len(indices)
        work_indices = [np.copy(indices[i]) for i in range(num_indices)]
        len_indices = len(work_indices[0])
        #only a single set of random numbers, then choose all the same positions
        choose_indices = np.where(np.random.uniform(size=len_indices) < q)
        if len(choose_indices) > 0:
            infected_indices = [work_indices[i][choose_indices[0]] for i in range(num_indices)]
            work_indices = tuple(infected_indices)
        else:
            work_indices = ()
        return work_indices  
