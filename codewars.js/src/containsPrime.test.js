const isPrime = require('./containsPrime');

test('should return true', () => {
  expect(isPrime('optimusprime')).toBeTruthy();
  // Test.assertEquals(isPrime('optimusprime'),true,'A prime is present');
  //     Test.assertEquals(isPrime('11'),true,'A prime is present');
  //     Test.assertEquals(isPrime('4'),false,'No prime has been found');
  //     Test.assertEquals(isPrime('starPrime'),true,'A prime is present');
  //     Test.assertEquals(isPrime('11aagghh4'),true,'A prime is present');
});
