const solve = (x) =>
  x.match(/([aeiou]+)/g).sort((a, b) => b.length - a.length)[0].length;

module.exports = solve;
