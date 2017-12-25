tape = []
cur = 0

def state_a():
    global tape, cur
    next_state = None
    if tape[cur] == 0:
        tape[cur] = 1
        cur += 1
        next_state = 'b'
    else:
        tape[cur] = 0
        cur += 1
        next_state = 'c'
    return next_state

def state_b():
	global cur, tape
	next_state = None
	if tape[cur] == 0:
		cur -= 1
		next_state = 'a'
	else:
		tape[cur] = 0
		cur += 1
		next_state = 'd'
	return next_state

def state_c():
    global cur, tape
    next_state = None
    if tape[cur] == 0:
        tape[cur] = 1
        cur += 1
        next_state = 'd'
    else:
        cur += 1
        next_state = 'a'
    return next_state

def state_d():
    global cur, tape
    next_state = None
    if tape[cur] == 0:
        tape[cur] = 1
        cur -= 1
        next_state = 'e'
    else:
        tape[cur] = 0
        cur -= 1
        next_state = 'd'
    return next_state

def state_e():
    global cur, tape
    next_state = None
    if tape[cur] == 0:
        tape[cur] = 1
        cur += 1
        next_state = 'f'
    else:
        cur -= 1
        next_state = 'b'
    return next_state

def state_f():
    global cur, tape
    next_state = None
    if tape[cur] == 0:
        tape[cur] = 1
        cur += 1
        next_state = 'a'
    else:
        cur += 1
        next_state = 'e'
    return next_state

states = {}
states['a'] = state_a
states['b'] = state_b
states['c'] = state_c
states['d'] = state_d
states['e'] = state_e
states['f'] = state_f

if __name__ == '__main__':
	steps = 12_368_930
	tape = [0] * 1_000_000_000
	cur = 1_000_000_00 // 2
	next_state = 'a'
	for step in range(steps):
		next_state = states[next_state]()
	print(sum(tape))


