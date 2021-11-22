tuplist = [(30, 420, 55), (96, 87, 54), (123, 456, 789)]
print([tups[:-1] + (100,) for tups in tuplist])
