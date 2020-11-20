const solve = require('../longestVowelChain');

test('codewarriors should return 2', () => {
  expect(solve('codewarriors')).toBe(2);
});

test('suoidea should return 3', () => {
  expect(solve('suoidea')).toBe(3);
});

test('ultrarevolutionariees should return 3', () => {
  expect(solve('ultrarevolutionariees')).toBe(3);
});

test('strengthlessnesses should return 1', () => {
  expect(solve('strengthlessnesses')).toBe(1);
});

test('cuboideonavicuare should return 2', () => {
  expect(solve('cuboideonavicuare')).toBe(2);
});

test('chrononhotonthuooaos shoulde return 5', () => {
  expect(solve('chrononhotonthuooaos')).toBe(5);
});

test('iiihoovaeaaaoougjyaw should return 8', () => {
  expect(solve('iiihoovaeaaaoougjyaw')).toBe(8);
});
