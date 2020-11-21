var vowels = 'aeiou';

// turn vowels into numbers
function encode(s) {
  return s.replace(/[aeiou]/gi, function (c) {
    return vowels.indexOf(c) + 1;
  });
}

//turn numbers back into vowels
function decode(s) {
  return s.replace(/\d/g, function (n) {
    return vowels[n - 1];
  });
}

module.exports = {
  encode,
  decode,
};
