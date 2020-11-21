const nextBigger = require('../nextbigger');

test('12', () => {
  expect(nextBigger(12)).toEqual(21);
});
test('513', () => {
  expect(nextBigger(513)).toEqual(531);
});
test('2017', () => {
  expect(nextBigger(2017)).toEqual(2071);
});
test('441', () => {
  expect(nextBigger(414)).toEqual(441);
});
test('144', () => {
  expect(nextBigger(144)).toEqual(414);
});
test('123456789', () => {
  expect(nextBigger(123456789)).toEqual(123456798);
});
test('1234567890', () => {
  expect(nextBigger(1234567890)).toEqual(1234567908);
});
test('9876543210', () => {
  expect(nextBigger(9876543210)).toEqual(-1);
});
test('Lots of 9s', () => {
  expect(nextBigger(9999999999)).toEqual(-1);
});
test('59884848459853', () => {
  expect(nextBigger(59884848459853)).toEqual(59884848483559);
});
