import dimod

# State the problem that we want to solve is very easy
# We will start with a simple case

J = {(0,1):1}

h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("The model that we are going to solve is")
print(model)

# We can solve it exactly
from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("The exact solution is")
print(solution)


# Or with *simulated annealing* (a heuristic method used in classical computers)
sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("The solution with simulated annealing is")
print(response)
print()

# D-Wave's API key
API_TOKEN = ''
config = {'token': API_TOKEN}


# And, of course, with D-Wave's quantum computer
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler(**config))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)


# Let us now see a more complicated case 

J = {(0,1):1,(0,2):1,(1,2):1,(1,3):1,(2,4):1,(3,4):1}
h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
print("The model that we are going to solve is")
print(model)


# First, we solve it exactly
sampler = ExactSolver()
solution = sampler.sample(model)
print("The exact solution is")
print(solution)


# Now, with *simulated annealing*

sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("The solution with simulated annealing is")
print(response)


# Finally, we use the *quantum annealer* again

sampler = EmbeddingComposite(DWaveSampler(solver='Advantage_system1.1', **config))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)