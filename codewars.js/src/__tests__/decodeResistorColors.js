import { decodeResistorColors } from '../decodeResistorColors';

test('A resistor under 1000 ohms and with only three bands', () => {
  expect(decodeResistorColors('yellow violet black')).toEqual('47 ohms, 20%');
});

test('A resistor between 1000 and 999999 ohms, with a gold fourth band', () => {
  expect(decodeResistorColors('yellow violet red gold')).toEqual('4.7k ohms, 5%');
});

test('A resistor of 1000000 ohms or above, with a silver fourth band', () => {
  expect(decodeResistorColors('brown black green silver')).toEqual('1M ohms, 10%');
});
