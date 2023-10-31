  export default class Interpreter {
    constructor() { 
        this.output = '';
        this.debug = [];
    }
    
    read(input){
        this.output = '';
        this.debug = [];
        let accumulator = 0;
        let pc = 0;
        let asciiMode = false;
        while(pc < input.length) {
            switch(input[pc]) {
                case 'a':
                    accumulator++;
                    break;
                case 'b':
                    accumulator--;
                    break;
                case 'c':
                    this.output += asciiMode ? String.fromCharCode(accumulator) : accumulator.valueOf().toString();
                    break;
                case 'd':
                    accumulator *= -1;
                    break;
                case 'l':
                    input = input.slice(0, pc) + input.substring(pc + 1);
                    pc = -1;
                    break;
                case 'n':
                    accumulator = 0;
                    break;
                case 'r':
                    accumulator = Math.floor(Math.random() * accumulator + 1);
                    break;
                case '$':
                    asciiMode = !asciiMode;
                    break;
                case ';':
                    this.debug.push(`${accumulator}->${String.fromCharCode(accumulator)}`);
                    break;
                default:
                    break;
            }
            pc++;
        }
        return this;
    }
  }