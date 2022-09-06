export function solve (x) {
  return x.match(/([aeiou]+)/g).sort((a, b) => b.length - a.length)[0].length;
}
