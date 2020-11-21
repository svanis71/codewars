const encode = require('../theVowelCode').encode;
const decode = require('../theVowelCode').decode;

test('encode hello', () => {
  expect(encode('hello')).toBe('h2ll4');
});

test('encode How are you today?', () => {
  expect(encode('How are you today?')).toBe('H4w 1r2 y45 t4d1y?');
});

test('encode This is an encoding test.', () => {
  expect(encode('This is an encoding test.')).toBe('Th3s 3s 1n 2nc4d3ng t2st.');
});

test('decode h2ll4', () => {
  expect(decode('h2ll4')).toBe('hello');
});
