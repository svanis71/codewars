import { productFib } from '../productFib';

test('4895', () => {
  expect(productFib(4895)).toEqual([55, 89, true]);
});

test('5895', () => {
  expect(productFib(5895)).toEqual([89, 144, false]);
});

test('74049690', () => {
  expect(productFib(74049690)).toEqual([6765, 10946, true]);
});

test('84049690', () => {
  expect(productFib(84049690)).toEqual([10946, 17711, false]);
});

test('193864606', () => {
  expect(productFib(193864606)).toEqual([10946, 17711, true]);
});

test('447577', () => {
  expect(productFib(447577)).toEqual([610, 987, false]);
});

test('602070', () => {
  expect(productFib(602070)).toEqual([610, 987, true]);
});
