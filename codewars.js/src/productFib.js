export function productFib(prod) {
  let fibNr1 = 0;
  let fibNr2 = 1;
  while (fibNr1 * fibNr2 < prod) {
    var next = fibNr1 + fibNr2;
    fibNr1 = fibNr2;
    fibNr2 = next;
  }
  return [fibNr1, fibNr2, fibNr1 * fibNr2 == prod];
}

