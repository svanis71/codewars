const PrimeFactorizer = require('../primefactorizer').PrimeFactorizer;

test('', () => {
  expect(new PrimeFactorizer(13).factor).toEqual({ 13: 1 });
});
test('', () => {
  expect(new PrimeFactorizer(24).factor).toEqual({ 2: 3, 3: 1 });
});
test('', () => {
  expect(new PrimeFactorizer(32767).factor).toEqual({ 7: 1, 31: 1, 151: 1 });
});
test('', () => {
  expect(new PrimeFactorizer(10000000001).factor).toEqual({
    101: 1,
    3541: 1,
    27961: 1,
  });
});
test('', () => {
  expect(new PrimeFactorizer(10967535067).factor).toEqual({
    104723: 1,
    104729: 1,
  });
});
