const encodeResistorColors = require('../encodeResistorColors');

test('10 ohms', () => {
  expect(encodeResistorColors('10 ohms')).toEqual('brown black black gold');
});

test('47 ohms', () => {
  expect(encodeResistorColors('47 ohms')).toEqual('yellow violet black gold');
});

test('100 ohms', () => {
  expect(encodeResistorColors('100 ohms')).toEqual('brown black brown gold');
});

test('220 ohms', () => {
  expect(encodeResistorColors('220 ohms')).toEqual('red red brown gold');
});

test('330 ohms', () => {
  expect(encodeResistorColors('330 ohms')).toEqual('orange orange brown gold');
});

test('470 ohms', () => {
  expect(encodeResistorColors('470 ohms')).toEqual('yellow violet brown gold');
});

test('680 ohms', () => {
  expect(encodeResistorColors('680 ohms')).toEqual('blue gray brown gold');
});

test('1k ohms', () => {
  expect(encodeResistorColors('1k ohms')).toEqual('brown black red gold');
});

test('4.7k ohms', () => {
  expect(encodeResistorColors('4.7k ohms')).toEqual('yellow violet red gold');
});

test('10k ohms', () => {
  expect(encodeResistorColors('10k ohms')).toEqual('brown black orange gold');
});

test('22k ohms', () => {
  expect(encodeResistorColors('22k ohms')).toEqual('red red orange gold');
});

test('47k ohms', () => {
  expect(encodeResistorColors('47k ohms')).toEqual('yellow violet orange gold');
});

test('100k ohms', () => {
  expect(encodeResistorColors('100k ohms')).toEqual('brown black yellow gold');
});

test('330k ohms', () => {
  expect(encodeResistorColors('330k ohms')).toEqual(
    'orange orange yellow gold',
  );
});

test('1M ohms', () => {
  expect(encodeResistorColors('1M ohms')).toEqual('brown black green gold');
});

test('2M ohms', () => {
  expect(encodeResistorColors('2M ohms')).toEqual('red black green gold');
});

test('', () => {});
