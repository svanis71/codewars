const fact = require('./factorial');

function n_over_k(n, k) {
  return fact(n) / (fact(k) * fact(n - k));
}

module.exports = n_over_k;
