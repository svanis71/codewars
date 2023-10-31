import FiveCommands from '../kyu5/five_command_lang';

describe('Fixed Tests should return', () => {
    var inter = new FiveCommands();
    test('the number 1 as a number', () => {
        expect(inter.read('^*').output).toEqual('1'); 
    });

    test('the number 2 as a number', () => {
        expect(inter.read('^^*').output).toEqual('2');
    });
    test('the number 3 as a number', () => {
            expect(inter.read('+^^^-^v*+*').output).toEqual('03');
    });
    test('the number 4 as a number', () => {
        expect(inter.read('++++^--^^^++*--*').output).toEqual('13');
    });
    test('the number 5 as a number', () => {
        expect(inter.read('++++++++++^^^^*^^^--^*^').output).toEqual('41'); 
    });
});

describe('Debug Tests should return', () => {
    var inter = new FiveCommands();
    test('the number 1 as a number', () => {
        expect(inter.read('^*', true).debug).toEqual(['0->1']); 
    });

    test('the number 2 as a number', () => {
        expect(inter.read('^^*', true).debug).toEqual(['0->2']);
    });
    test('the number 3 as a number', () => {
            expect(inter.read('+^^^-^v*+*', true).debug).toEqual(['0->0','1->3']);
    });
    test('the number 4 as a number', () => {
        expect(inter.read('++++^--^^^++*--*', true).debug).toEqual(['0->0','1->0','2->3','3->0','4->1']);
    });
    test('the number 5 as a number', () => {
        expect(inter.read('++++++++++^^^^*^^^--^*^', true).debug).toEqual(['0->0','1->0','2->0','3->0','4->0','5->0','6->0','7->0','8->2','9->0','10->7']); 
    });
});

    // it("Debug Tests", () => {
    //   Test.assertSimilar(inter.read('^*',true, true).debug,['0->1'],'Should return the number 1 as a number');
    //   Test.assertSimilar(inter.read('^^*',true, true).debug,["0->2"],'Should return the number 2 as a number');
    //   Test.assertSimilar(inter.read('+^^^-^v*+*',true, true).debug, ["0->0","1->3"],'Should return the number 3 as a number');
    //   Test.assertSimilar(inter.read('++++^--^^^++*--*',true, true).debug,["0->0","1->0","2->3","3->0","4->1"],'Should return the number 4 as a number');
    //   Test.assertSimilar(inter.read('++++++++++^^^^*^^^--^*^',true, true).debug,["0->0","1->0","2->0","3->0","4->0","5->0","6->0","7->0","8->2","9->0","10->7"],'Should return the number 5 as a number');
    // });
