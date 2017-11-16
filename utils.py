# Utilities for the sudoku solver
#
from functools import reduce

rows = 'ABCDEFGHI'
cols = '123456789'

# function to cross the rows and cols
def cross(a, b):
    return [s + t for s in a for t in b]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

print(peers['A1'])
def grid_values(grid):
    dic = {}
    for x,y in zip(boxes, grid):
        dic[x] = y
        if y == '.':
            dic[x] = '123456789'
    return dic

def display(grid_values):
    string = ''
    for r in rows:
        for c in cols:
            string += grid_values[r+c] + ' '
            if c == '3' or c == '6':
                string += '|'
            if c == '9':
                string += '\n'
            if (r == 'C' or r == 'F') and c == '9':
                string += '------+------+------\n'
    print(string)
    
def eliminate(values):

    for box in values:
        if len(values[box]) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(values[box], '')
    return values


def only_choice(values):

    for box in values:
        for char in values[box]:
            if len(values[box]) > 1:
                for r_unit in unitlist:
                    if box in r_unit:
                        string = ''
                        for cell in r_unit:
                            string += values[cell]                  
                        if string.count(char) == 1:
                            values[box] = char
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False
    if len(reduce(lambda x,y: x+y, values.values())) == 81:
        return values
    sorted_values = list(filter(lambda y: len(y[1]) > 1,sorted(values.items(), key=lambda x: len(x[1]))))

    for char in values[sorted_values[0][0]]:
        new_value = values.copy()
        new_value[sorted_values[0][0]] = char
        attempt = search(new_value)
        display(new_value)
        if attempt:
            return attempt
        
def naked_twin(values):
    # check each field in the board
    for box in values:
        # if a field has len == 2, it can be a naked twin
        if len(values[box]) == 2:
            # separeta all peers of the field, but must be checked one each time
            peers_box = [n for n in unitlist if box in n]
            # iterate each unit
            for unit in peers_box:
                # create a dict to count
                val_unit = {k:values[k] for k in values if k in unit}
                # if there is a naked twin
                if list(val_unit.values()).count(values[box]) == 2:
                    # itarete each peer box
                    for field in unit:
                        if len(values[field]) > 2 and values[box][0] in values[field] and values[box][1] in values[field]:
                            # just replace if there are more than the two char in the field
                            for char in values[box]:
                                values[field] = values[field].replace(char, '')
        
    
        

        
        
        
        
        
        