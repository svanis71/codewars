import { interpreter } from '../smallfuck';

test('should work for some example test cases', function () {
    // Flips the leftmost cell of the tape
    expect(interpreter('*', '00101100')).toEqual('10101100');
    // Flips the second and third cell of the tape
    expect(interpreter('>*>*', '00101100')).toEqual('01001100');
    // Flips all the bits in the tape
    expect(interpreter('*>*>*>*>*>*>*>*', '00101100')).toEqual('11010011');
    // Flips all the bits that are initialized to 0
    expect(interpreter('*>*>>*>>>*>*', '00101100')).toEqual('11111111');
    // Goes somewhere to the right of the tape and then flips all bits that are initialized to 1, progressing leftwards through the tape
    expect(interpreter('>>>>>*<*<<*', '00101100')).toEqual('00000000');
});
test('should ignore all non-command characters', function () {
    expect(interpreter('iwmlis *!BOSS 333 ^v$#@', '00101100')).toEqual('10101100');
    expect(interpreter('>*>*;;;.!.,+-++--!!-!!!-', '00101100')).toEqual('01001100');
    expect(interpreter(`    *  >
    *           >
    
*>*lskdfjsdklfj>*;;+--+--+++--+-+-  lskjfiom,x  
>*sdfsdf>sdfsfsdfsdfwervbnbvn*,.,.,,.,.  >


*`, '00101100')).toEqual('11010011');
    expect(interpreter('*,,...,..,..++-->++++-*>--+>*>+++->>..,+-,*>*', '00101100')).toEqual('11111111');
    expect(interpreter('>>nssewww>>wwess>*<nnn*<<ee*', '00101100')).toEqual('00000000');
});
test('should return the final state of the tape immediately if the pointer ever goes out of bounds', function () {
    expect(interpreter('*>>>*>*>>*>>>>>>>*>*>*>*>>>**>>**', '0000000000000000')).toEqual('1001101000000111');
    expect(interpreter('<<<*>*>*>*>*>>>*>>>>>*>*', '0000000000000000')).toEqual('0000000000000000');
    expect(interpreter('*>*>*>>>*>>>>>*<<<<<<<<<<<<<<<<<<<<<*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*>*>*', '11111111111111111111111111111111')).toEqual('00011011110111111111111111111111');
    expect(interpreter('>>*>*>*<<*<*<<*>*', '1101')).toEqual('1110');
});
test('should work for some simple and nested loops', function () {
    expect(interpreter('*[>*]', '0'.repeat(256))).toEqual('1'.repeat(256));
    expect(interpreter('[>*]', '0'.repeat(256))).toEqual('0'.repeat(256));
    expect(interpreter('*>*>>>*>*>>>>>*>[>*]', '0'.repeat(256))).toEqual('11001100001' + '0'.repeat(245));
    expect(interpreter('*>*>>>*>*>>>>>*[>*]', '0'.repeat(256))).toEqual('11001100001' + '1'.repeat(245));
    expect(interpreter('*[>[*]]', '0'.repeat(256))).toEqual('1' + '0'.repeat(255));
    expect(interpreter('*[>[*]]', '1'.repeat(256))).toEqual('0' + '1'.repeat(255));
    expect(interpreter('[[]*>*>*>]', '000')).toEqual('000');
    expect(interpreter('*>[[]*>]<*', '100')).toEqual('100');
    expect(interpreter('[*>[>*>]>]', '11001')).toEqual('01100');
    expect(interpreter('[>[*>*>*>]>]', '10110')).toEqual('10101');
});
