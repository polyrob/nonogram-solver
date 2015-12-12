# nonogram-solver
Python nonogram solver. Written for puzzle from the UK’s intelligence agency, GCHQ.


```python
    while not solved:
        filter_possibles(board)
        apply_certainties(board)
```

Solved puzzle, processed through imaging software to apply threshold.
![Processed QR](https://github.com/polyrob/nonogram-solver/blob/master/qr.jpg)


Actual console output:
```
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
