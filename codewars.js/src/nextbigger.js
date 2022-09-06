export function nextBigger(n) {
  let digs = n.toString().split('');
  const org = digs.slice(0);
  let pos = 0;
  for (let i = digs.length - 1; i > 0; i--) {
    if (digs[i] > digs[i - 1]) {
      const tmp = digs[i - 1];
      digs[i - 1] = digs[i];
      digs[i] = tmp;
      pos = i;
      break;
    }
  }
  const tail = digs.splice(pos - 1).sort();
  const m = tail.findIndex(function (n) {
    return n > org[pos - 1];
  });
  tail.unshift(tail.splice(m, 1)[0]);
  digs = digs.concat(tail);
  const next = parseInt(digs.join(''));
  return next == n ? -1 : next;
}
