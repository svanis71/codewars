export function encodeResistorColors(ohmsString) {
  const colorMap = {
    0: 'black', 1: 'brown', 2: 'red',
    3: 'orange', 4: 'yellow', 5: 'green',
    6: 'blue', 7: 'violet', 8: 'gray',
    9: 'white',
  };
  ohmsString = ohmsString.replace(/\s?ohms$/, '').replace('k', '000').replace('M', '000000');
  if (ohmsString.includes('.')) {
    ohmsString = ohmsString.replace('.', '').replace(/0$/, '');
  }
  const [n1, n2] = ohmsString.substr(0, 2);
  const colors = [colorMap[n1], colorMap[n2], colorMap[ohmsString.length - 2]];
  return `${colors.join(' ')} gold`;
}
