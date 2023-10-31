export default class FiveCommands {
    constructor() {}

    read(code, debug_mode) {
        this.output = '';
        this.debug = [];
        const tape = [0];
        let ptr = 0;
        for(let i = 0; i < code.length; i++) {
            switch(code[i]) {
                case '+':
                    ptr++;
                    if(tape.length <= ptr) {
                        tape.push(0);
                    }
                    break;
                case '-':
                    ptr--;
                    if(ptr < 0) {
                        ptr = 0;
                        tape.unshift(0);
                    }
                    console.log(`move left to ${ptr} on ${tape}`);
                    break;
                case '^': tape[ptr]++; break;
                case 'v': tape[ptr]--; break;
                case '*': this.output += tape[ptr]; break;
            }
        }
        if(debug_mode === true) {
            this.debug = tape.map((v, i) => `${i}->${v}`);
        }
        return this;
    }
}
