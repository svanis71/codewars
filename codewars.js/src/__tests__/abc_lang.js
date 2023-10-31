import Interpreter from '../kyu4/abc_lang';

describe('Fixed Tests should', () => {
  var inter = new Interpreter();
  it('return the number 1337 as a string', () => {
    expect(inter.read('acaaccaaaac').output).toBe('1337');
  });
  it('output Hello, World!', () => {
    expect(
      inter.read(
        '$aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaccaaacbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaacaaacbbbbbbcbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc'
      ).output
    ).toBe('Hello, World!');
  });
  it('return the number 24-2 as a string', () => {
    expect(inter.read('aacaacnaadc').output).toBe('24-2');
  });
  it('return the number 1234 as a string', () => {
    expect(inter.read('acacacac').output).toBe('1234');
  });
  it('return the number 5 as a string', () => {
    expect(inter.read('aaaaac').output).toBe('5');
  });
});

describe('loop test', () => {
  var inter = new Interpreter();
  test('small loop', () => {
    expect(inter.read('allc').output).toEqual('3');
    expect(inter.read('alllc').output).toEqual('4');
    expect(inter.read('aaaaalllllaaac').output).toEqual('33');
  });
});

describe('Debug tests should return', () => {
  var inter = new Interpreter();
  test('[33->!]', () => {
    expect(inter.read('aaaaalllllaaa$c;').debug).toEqual(['33->!']);
  });
  test('[\'55->7\',\'60-><\',\'65->A\',\'70->F\',\'75->K\',\'80->P\',\'85->U\',\'90->Z\',\'95->_\']', () => {
    expect(inter.read('aaaaallllllllll;llllllllaa$c').debug).toEqual(['55->7','60-><','65->A','70->F','75->K','80->P','85->U','90->Z','95->_']);
  });
  test('[\'101->e\',\'102->f\']', () => {
    expect(inter.read('aaaaallllllaaaaalllllla;a;$c').debug).toEqual(['101->e','102->f']);
  });
  test('[\'78->N\',\'90->Z\',\'103->g\',\'117->u\']', () => {
    expect(inter.read('lalalalalalalalalalalala;lalala$c').debug).toEqual(['78->N','90->Z','103->g','117->u']);
  });
  test('[\'42->*\',\'54->6\',\'68->D\']', () => {
    expect(inter.read('laalaalaalaalaalaa;laalaa$c').debug).toEqual(['42->*','54->6','68->D']);
  });
});
