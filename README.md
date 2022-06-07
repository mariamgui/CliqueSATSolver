# Graph_Clique_SAT_Solver
This provides a SAT solver the graph clique problem which is an NP-hard problem. 

### What is a clique?
A clique in a graph is a subset of vertices, all adjacent to each other, also called complete subgraphs in the graph. 

### What you need to run this code? 
Make sure to run 
<code> export PYTHONPATH=$HOME/.smt_solvers/python_bindings </code>

Then install pysmt with the z3 solver.

<code> pysmt-install --z3 </code>

The choice of the solver is up to you. There exists many other solvers as well.
