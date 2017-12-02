# Exercício canibais Artificial Intelligence
# como passar 3 canibais e 3 missionários para o outro lado do rio
# em um barco que pode carregar uma ou duas pessoas
# sem deic=xar que tenham mais canibais que missionários em lugar nenhum

import random

class Location:
    def __init__(self, name, crowd):
        self.crowd = crowd
        self.name = name
    def count(self, person):
        return self.crowd.count(person)

class State:
    def __init__(self, begin, boat, finish):
        self.begin = begin
        self.boat = boat
        self.finish = finish
        self.history = [['begin']]
        
    def copy(self):
        new_state = State(Location('Start', self.begin.crowd.copy()),
                     Location('Boat', self.boat.crowd.copy()),
                     Location('Finish', self.finish.crowd.copy()))
        new_state.history = self.history.copy()
        return new_state
        
    def test_objective(self):
        return self.finish.count('Canibal') == self.finish.count('Missionario') == 3
    
    def test_fail(self):
        fail_boat = len(self.boat.crowd) > 2
        fail_begin = self.begin.count('Canibal') > self.begin.count('Missionario') > 0
        fail_finish = self.finish.count('Canibal') > self.finish.count('Missionario') > 0
        return fail_boat or fail_begin or fail_finish

    def queue_maker(self):
        queue = []
        current_heur = self.heuristc()
        for person in set(self.begin.crowd):
            queue.append([0, 1, person, 1 + current_heur])
        for person in set(self.boat.crowd):
            queue.append([1, 0, person, 0 + current_heur])
            queue.append([1, 2, person, 1 + current_heur])
        for person in set(self.finish.crowd):
            queue.append([2, 1, person, 0 + current_heur])
        return sorted(queue, key = lambda x: x[3], reverse=True)
    
    
    def heuristc(self):
        return len(self.boat.crowd) + (len(self.finish.crowd) * 2)

init_state = State(Location('Start', ['Missionario', 'Missionario', 'Missionario', 'Canibal', 'Canibal', 'Canibal']), 
                   Location('Boat', []),
                   Location('Finish', []))

def action(orig, dest, person, state):
    locations = [state.begin, state.boat, state.finish]
    origin = locations[orig]
    destination = locations[dest]
    destination.crowd += [origin.crowd.pop(origin.crowd.index(person))]
    state.history += [[origin.name, destination.name, person,
                       (state.begin.crowd.count('Missionario'),state.begin.crowd.count('Canibal')),
                       (state.boat.crowd.count('Missionario'),state.boat.crowd.count('Canibal')),
                       (state.finish.crowd.count('Missionario'),state.finish.crowd.count('Canibal'))]]
    
def deep_search(state):
    if state.test_fail() or [l[3:] for l in state.history].count(state.history[-1][3:]) > 1:
        return False
    if state.test_objective():
        return state.history
    queue = state.queue_maker()
    for move in queue:
        new_state = state.copy()
        action(move[0], move[1], move[2], new_state)
        next_step = deep_search(new_state)
        if next_step:
            return next_step

result = deep_search(init_state)

queue = init_state.queue_maker()