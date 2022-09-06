import { isPrime } from '../containsPrime';

test('optimusprime should return true', () => {
  expect(isPrime('optimusprime')).toBeTruthy();
});
test('11 should return true', () => {
  expect(isPrime('11')).toBeTruthy();
});
test('starPrime should return true', () => {
  expect(isPrime('starPrime')).toBeTruthy();
});
test('11aagghh4 should return true', () => {
  expect(isPrime('11aagghh4')).toBeTruthy();
});

test('4 should return false', () => {
  expect(isPrime('4')).toBeFalsy();
});
