function nextBigger(n) {
  var digs = n.toString().split('');
  var org = digs.slice(0);
  for (var i = digs.length - 1; i > 0; i--) {
    if (digs[i] > digs[i - 1]) {
      var tmp = digs[i - 1];
      digs[i - 1] = digs[i];
      digs[i] = tmp;
      break;
    }
  }
  var tail = digs.splice(i - 1).sort();
  var m = tail.findIndex(function (n) {
    return n > org[i - 1];
  });
  tail.unshift(tail.splice(m, 1)[0]);
  digs = digs.concat(tail);
  var next = parseInt(digs.join(''));
  return next == n ? -1 : next;
}

module.exports = nextBigger;