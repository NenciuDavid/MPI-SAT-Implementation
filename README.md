# MPI-SAT-Implementation
In this study, the author explores different techniques for improving the
efficiency of satisfiability solving algorithms. The goal is to compare the
efficiency of existing algorithms by focusing on variable selection strategies
during the solving process to reduce computational time and improve
performance. Experimental evaluation demonstrates that the proposed
method outperforms classic algorithms in certain cases.
System manual
• The project’s files:
– README.md - short description of the project, including the system
manual
– datasets.txt - file containing some of the datasets used in the experiment, in order to help recreate the experiment if needed
– main.py - the main file with the implementation of all the algorithms
presented in the paper
– results.csv - the file with the results of the current dataset, shown
in .csv format
• The modeling of the data
1. Literals are represented by strings, because the program accepts both
letters and numbers as input data
2. Clauses are represented by sets of literals. The use of sets has the
advantage that they are unordered data structures, but it also has
the disadvantage that they are randomly ordered every time, making
the results differ between runs
3. Sets of Clauses are represented by lists, because the need of an ordered data structure
• Functions from main.py
1. init csv() - creates the csv file for the results
2. saveResult() - updates the csv file with the results from that run
3. complement() - returns the complement of that literal
4. resolution() - the main function for the resolution algorithm that
returns the result of that algorithm
5. findResolvent() - Used to find a random resolvent from the set of
clauses. Called in resolution()
6. isRez() - Used to verify if a two clauses have a resolvent and return
that resolvent. Called in findResolvent() and findResolventShortestPair()
7. findResolventShortesPair() - used to find the resolvent of the
clauses that have the smallest length. Called in resolutionShortestPair()
8. resolutionShortestPair() - the main function of the improvement
of classic resolution, by adding the condition that the pair of clauses
that we choose for our resolvent must have the smallest length
9. davisPutnam() - the main function of the Davis Putnam algorithm
that returns true if that set of clauses is satisfiable or false otherwise
10. verifyOneLiteralRule() - used to verify if the one literal rule is
applicable. Called in davisPutnam(), davisPutnamShortestPair(),
DPLL()
11. applyOneLiteralRule() - used to apply one literal rule on the set
of clauses. Called in davisPutnam(), davisPutnamShortestPair(),
DPLL()
12. verifyPureLiteralRule() - used to verify if pure literal rule is
applicable. Called in davisPutnam(), davisPutnamShortestPair(),
DPLL()
13. applyPureLiteralRule() - used to apply pure literal rule on the
set of clauses. Called in davisPutnam(), davisPutnamShortestPair(),
DPLL()
14. davisPutnamShortestPair() - the main function of the improvement of Davis Putnam algorithm. Insead of calling resolution() at
step 3, it calls resolutionShortestPair()
15. DPLL() - the main function of the Davis Putnam Logemann Loveland,
that return the result of the algorithm
16. MOMS() - used to find the literal with the maximum occurrences in
clauses of minimal size. Used in DPLLMOMS()
17. DPLLMOMS() - the main function of the improvement of DPLL. Instead
of choosing a random literal for splitting at rule 3, it chooses the
literal with the maximum occurrences in clauses of minimal size
User manual
– Repository link: https://github.com/NenciuDavid/MPI-SAT-Implementation
– Clone the project:
git clone https://github.com/NenciuDavid/MPI-SAT-Implementation
– Dependencies: Python 3.10+ (no more libraries are needed, only
the basic python libraries)
7
– In order to run the program, it is only necessary to run
main.py
– Input data: The program accepts inputs under the form: each
clause needs to be written on a line, the literals must be separated
by space, and the literals can be both letters and numbers. The
negation of a literal has the prefix -. After the last clause, the user
needs to input a 0 in order to stop the reading of clauses.
– Output data:
1. .csv file - The program outputs the algorithms used to find
the satisfiability of that set of clauses, the result, how many
seconds did each algorithm need to get to the result, and the
peak memory usage of each algorithm.
2. Console prints - The program outputs the same information
as in the .csv file, but with a few additions, such as: the number
of steps needed to get to the result, and the sets of clauses after
each step.