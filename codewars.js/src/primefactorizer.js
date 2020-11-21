function PrimeFactorizer(n) {
  var factors = {};

  var _isPrime = function (n) {
    if (n == 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    var root = Math.floor(Math.sqrt(n));
    var isPrime = true;
    for (var i = 3; i < root && isPrime; i += 2) {
      if (n % i == 0) isPrime = false;
    }
    return isPrime;
  };

  var _generatePrimes = function (max) {
    var primes = [2];
    for (var i = 3; i < max; i += 2) {
      if (_isPrime(i)) {
        primes.push(i);
      }
    }
    return primes;
  };

  var _factor = function (n) {
    if (_isPrime(n)) {
      factors[n.toString()] = 1;
    } else {
      var primes = _generatePrimes(Math.sqrt(n));
      var rest = n;
      for (var i = 0; i < primes.length && rest > 1; i++) {
        while (rest % primes[i] == 0 && rest > 1) {
          factors[primes[i].toString()] =
            (factors[primes[i].toString()] || 0) + 1;
          rest = rest / primes[i];
        }
      }
    }
    if (rest > 0 && _isPrime(rest)) {
      factors[rest.toString()] = (factors[rest.toString()] || 0) + 1;
    }
  };

  _factor(n);

  return { factor: factors };
}

module.exports = { PrimeFactorizer };
