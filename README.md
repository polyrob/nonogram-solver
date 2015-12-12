# nonogram-solver
Python nonogram solver. This was was written for a puzzle from the UK’s intelligence agency, GCHQ that was posted on Gizmodo [here](http://gizmodo.com/can-you-solve-the-uk-intelligence-agencys-christmas-puz-1747265899).

This program trys to solve it similarly to how I would - by determining the possible configurations for a column/row, and then marking what you know to be true. Each time looping through you should have a little more information in order to narrow down the possiblities.  The loop is basically this:
```python
    while not solved:
        filter_possibles(board)
        apply_certainties(board)
```
For this puzzle, it was solved in 8 iterations through the rows and columns.

Solved puzzle, processed through imaging software to apply threshold.
![Processed QR](https://github.com/polyrob/nonogram-solver/blob/master/qr.jpg)


Here is the actual console output after the program is run:
```
...
== COMPLETE ==

	███████░███░░░█░█░███████
	█░░░░░█░██░██░░░░░█░░░░░█
	█░███░█░░░░░███░█░█░███░█
	█░███░█░█░░██████░█░███░█
	█░███░█░░█████░██░█░███░█
	█░░░░░█░░██░░░░░░░█░░░░░█
	███████░█░█░█░█░█░███████
	░░░░░░░░███░░░███░░░░░░░░
	█░██░███░░█░█░███░█░░█░██
	█░█░░░░░░███░██░░░░█░░░█░
	░████░█░████░██░█░░░░██░░
	░█░█░░░█░░░█░█░████░█░███
	░░██░░█░█░█░░░░░░██░█████
	░░░███░██░██░██████░███░█
	█░█████████░█░█░░██░░░░█░
	░██░█░░██░░░██░███░░░░░█░
	███░█░█░█░░█░░░░█████░█░░
	░░░░░░░░█░░░██░██░░░█████
	███████░█░░██░░░█░█░█░███
	█░░░░░█░██░░█░░██░░░██░█░
	█░███░█░░░████░░█████░░█░
	█░███░█░███░██████████░██
	█░███░█░█░░██████░██████░
	█░░░░░█░░██░░░░░░█░█░██░░
	███████░██░░░█░██░░░█████

*=*=*=* SUCCESS *=*=*=*
Iteration 8, Time elapsed (sec): 1.796
```
