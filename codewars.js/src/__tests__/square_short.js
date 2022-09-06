import { sq } from '../sq';

test('Must be less than 40 chars', () => {
  expect(sq.toString().length + 3).toBeLessThan(40);
});

test('0', () => {
  expect(sq(0)).toBe(0);
});
test('1', () => {
  expect(sq(1)).toBe(1);
});
test('2', () => {
  expect(sq(2)).toBe(4);
});
test('3', () => {
  expect(sq(3)).toBe(9);
});
test('4', () => {
  expect(sq(4)).toBe(16);
});
test('4.4', () => {
  expect(sq(4.4)).toBe(19);
});
test('-4.44', () => {
  expect(sq(-4.44)).toBe(20);
});
test('32768', () => {
  expect(sq(32768)).toBe(1073741824);
});
