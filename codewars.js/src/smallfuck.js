const findMatchingCloseBracket = (arr, start) => {
    let bracketCount = 1;
    let pc = start + 1;
    for(; bracketCount > 0 && pc < arr.length; pc++) {
        if(arr[pc] === '[') {
            bracketCount++;
        }
        if(arr[pc] === ']') {
            bracketCount--;
        }
    }
    return pc;
};

const findMatchingOpenBracket = (arr, start) => {
    let bracketCount = 1;
    let pc = start - 1;
    for(; bracketCount > 0 && pc >= 0; pc--) {
        if(arr[pc] === '[') {
            bracketCount--;
        }
        if(arr[pc] === ']') {
            bracketCount++;
        }
    }
    return pc + 1;
};
export function interpreter (code, tape) {
  let instructions = code.split('');
  let bits = tape.split('').map(p => parseInt(p));
  let pc = 0;
  let cell = 0;
  while(cell >= 0 && cell < bits.length && pc < instructions.length) {
      switch(instructions[pc]) {
        case '*':
          bits[cell] = ~bits[cell] & 0x1;
          pc++;
          break;
        case '>':
          cell++;
          pc++;
          break;
        case '<':
          cell--;
          pc++;
          break;
        case '[':
            if(!bits[cell]) {
              pc = findMatchingCloseBracket(instructions, pc);
            }
            else {
                pc++;
            }
            break;
        case ']':
            if(bits[cell]) {
              pc = findMatchingOpenBracket(instructions, pc);
            }
            else {
                pc++;
            }
          break;
        default:
          pc++;
          break;
      }
  }
  return bits.join('');
}
