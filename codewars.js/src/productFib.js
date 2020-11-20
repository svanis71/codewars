function productFib(prod) {
  var fibNr1 = 0;
  var fibNr2 = 1;
  while (fibNr1 * fibNr2 < prod) {
    var next = fibNr1 + fibNr2;
    fibNr1 = fibNr2;
    fibNr2 = next;
  }
  return [fibNr1, fibNr2, fibNr1 * fibNr2 == prod];
}

module.exports = productFib;
