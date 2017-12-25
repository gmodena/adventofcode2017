class TuringMachine:
    def __init__(self):
        self.tape = [0]
        self.cur = 0
        self.states = {}
        self.states['a'] = self.state_a
        self.states['b'] = self.state_b
        self.states['c'] = self.state_c
        self.states['d'] = self.state_d
        self.states['e'] = self.state_e
        self.states['f'] = self.state_f
        self.next_state = 'a'

    def state_a(self):
        if self.tape[self.cur] == 0:
            self.tape[self.cur] = 1
            self.cur += 1
            self.next_state = 'b'
        else:
            self.tape[self.cur] = 0
            self.cur += 1
            self.next_state = 'c'

    def state_b(self):
        if self.tape[self.cur] == 0:
            self.cur -= 1
            self.next_state = 'a'
        else:
            self.tape[self.cur] = 0
            self.cur += 1
            self.next_state = 'd'

    def state_c(self):
        if self.tape[self.cur] == 0:
            self.tape[self.cur] = 1
            self.cur += 1
            self.next_state = 'd'
        else:
            self.cur += 1
            self.next_state = 'a'

    def state_d(self):
        if self.tape[self.cur] == 0:
            self.tape[self.cur] = 1
            self.cur -= 1
            self.next_state = 'e'
        else:
            self.tape[self.cur] = 0
            self.cur -= 1
            self.next_state = 'd'

    def state_e(self):
        if self.tape[self.cur] == 0:
            self.tape[self.cur] = 1
            self.cur += 1
            self.next_state = 'f'
        else:
            self.cur -= 1
            self.next_state = 'b'

    def state_f(self):
        if self.tape[self.cur] == 0:
            self.tape[self.cur] = 1
            self.cur += 1
            self.next_state = 'a'
        else:
            self.cur += 1
            self.next_state = 'e'

    def run(self, steps=0):
        self.tape = [0] * steps
        self.cur = steps // 2
        for step in range(steps):
            if self.cur < 0:
                self.tape.insert(0, 0)
            elif self.cur >= len(self.tape):
                self.tape.append(0)
            self.states[self.next_state]()
    def checksum(self):
        return(sum(self.tape))
if __name__ == '__main__':
    tm = TuringMachine()
    tm.run(steps=12_368_930)
    print(tm.checksum())


