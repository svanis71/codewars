const _isPrime = (i, o) => {
  if (i * i <= o) {
    return o % i != 0 && _isPrime(i + 2, o);
  }
  return true;
};

export function isPrime (s) {
  return s.search(/prime/i) > -1 ||
    s.split(/[^0-9]+/)
    .map((x) => ~~x)
    .filter((x) => x == 2 || (x > 2 && x % 2 != 0))
    .some((x) => _isPrime(3, x));
}
