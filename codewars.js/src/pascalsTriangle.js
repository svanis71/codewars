const n_over_k = require('./n_over_k');

function pascalsTriangle(n) {
  //return a flat array representing the values of Pascal's Triangle to the n-th level
  var triangle = [];
  for (var level = 0; level < n; level++) {
    for (var c = 0; c <= level; c++) {
      var noverk = Math.round(n_over_k(level, c));
      triangle.push(noverk);
    }
  }
  return triangle;
}

module.exports = pascalsTriangle;
