export function decodeResistorColors(bands) {
  // Most resistors will also have a fourth band that is either gold or silver,
  // with gold indicating plus or minus 5% tolerance,
  // silver indicating 10% tolerance.
  // Resistors that do not have a fourth band are rated at 20% tolerance
  const colors = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'gray',
    'white',
  ];
  const tolerences = {
    gold: '5%',
    silver: '10%',
    black: '20%',
  };
  const [band1, band2, zeros, tolerance] = bands.split(' ');

  let ohms = +`${colors.indexOf(band1)}${colors.indexOf(band2)}`.padEnd(
    2 + colors.indexOf(zeros),
    '0',
  );
  let unit = '';
  if (ohms > 999999) {
    ohms /= 1000000;
    unit = 'M';
  }
  if (ohms > 999) {
    ohms /= 1000;
    unit = 'k';
  }

  return `${ohms}${unit} ohms, ${tolerences[tolerance || 'black']}`;
}
