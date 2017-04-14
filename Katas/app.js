function fact(n) {
    if (n <= 1)
        return 1;
    return n * fact(n - 1);
}

function n_over_k(n, k) {
    return fact(n) / (fact(k) * fact(n - k));
}

function pascalsTriangle(n) {
    //return a flat array representing the values of Pascal's Triangle to the n-th level
    var triangle = [];
    for (var level = 0; level < n; level++) {
        for (var c = 0; c <= level; c++) {
            var noverk = Math.round(n_over_k(level, c));
            console.log(level + ' over ' + c + ' = ' + noverk);
            triangle.push(noverk);
        }
    }
    return triangle;
}

function comp(array1, array2) {
    if (!array1 || !array2) return false;
    if (array1.length != array2.length) return false;
    var copy = array1.map(function (n) { return n * n; }).sort();
    array2.sort();
    for (var i = 0; i < array1.length; i++) {
        if (copy[i] != array2[i]) return false;
    }
    return true;
}

function comp2(array1, array2) {
    if (!array1 || !array2) return false;
    if (array1.length != array2.length) return false;
    array2.sort();
    return array1.map(function (n) { return n * n; }).sort().map(function (n, i) { return n == array2[i]; }).every(function (v) { return v === true; });
}

var vowelMapper = {
    a: 1,
    e: 2,
    i: 3,
    o: 4,
    u: 5,
    getVowel: function (n) {
        for (var p in this) {
            console.log(p, this[p]);
            if (this[p] == n) {
                return p;
            }
        }
        return undefined;
    }
};

var vowels = "aeiou";
// turn vowels into numbers
function encode(s) {
    return s.replace(/[aeiou]/gi, function (c) { return vowels.indexOf(c) + 1; })
}

//turn numbers back into vowels
function decode(s) {
    return s.replace(/\d/g, function (n) { return vowels[n - 1]; })
}

// console.log(encode('hello'));
// console.log(decode('h3 th2r2'));

//console.log(pascalsTriangle(5));
// var t = pascalsTriangle(25);
// for(var i = t.length - 25; i < t.length; i++) {
//     console.log(t[i]);
// }

// console.log(fact(24));
// console.log(fact(23));
// console.log(fact(1));
// console.log(n_over_k(24, 23));

// a1 = [121, 144, 19, 161, 19, 144, 19, 11];
// a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];
// console.log(comp2(a1,a2));

var Test = {
    assertEquals: function (a, b) {
        if (a === b) {
            console.log("OK!");
            return;
        }
        console.log("FAIL :-( expected: ", b, "was", a);
    },
    expect: function (b) {
        if (b === true) {
            console.log('OK!');
            return;
        }
        console.log('FAIL! :-( expected true but was false');
    }
}

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
    var m = tail.findIndex(function (n) { return n > org[i - 1]; });
    tail.unshift(tail.splice(m, 1)[0]);
    digs = digs.concat(tail);
    var next = parseInt(digs.join(''));
    return next == n ? -1 : next;
}

// Test.assertEquals(nextBigger(12),21)
// Test.assertEquals(nextBigger(513),531)
// Test.assertEquals(nextBigger(2017),2071)
// Test.assertEquals(nextBigger(414),441)
// Test.assertEquals(nextBigger(144),414)
// Test.assertEquals(nextBigger(1234567890), 1234567908);
// Test.assertEquals(nextBigger(59884848459853), 59884848483559);

String.prototype.toBase64 = function () {
    var base64Table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var charCodes = this.split('').map(function (c) { return c.charCodeAt(0); });
    var encodedString = '';

    for (var i = 0; i < charCodes.length; i += 3) {
        var base64Code = (charCodes[i] << 16) | ((charCodes[i + 1] << 8) || 0) | (charCodes[i + 2] || 0);
        encodedString += base64Table[(base64Code & 0xFC0000) >> 18];
        encodedString += base64Table[(base64Code & 0x03F000) >> 12];
        if (i + 1 < charCodes.length) {
            encodedString += base64Table[(base64Code & 0x000FC0) >> 6];
            if (i + 2 < charCodes.length) {
                encodedString += base64Table[base64Code & 0x3F];
            }
            else {
                encodedString += '=';
            }
        }
        else {
            encodedString += '==';
        }
    }
    return encodedString;
}

String.prototype.fromBase64 = function () {
    var base64Table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var encodedValues = this.split('').map(function (s1) { if (s1 != '=') { return base64Table.indexOf(s1); } return 0; });
    var decoded = '';

    for (var i = 0; i < encodedValues.length; i += 4) {
        var bits = encodedValues[i] << 18;
        bits |= ((encodedValues[i + 1] || 0) << 12);
        bits |= ((encodedValues[i + 2] || 0) << 6);
        bits |= (encodedValues[i + 3] || 0);
        decoded += String.fromCharCode((bits & 0xFF0000) >> 16);
        if ((bits & 0xFF00) > 0) {
            decoded += String.fromCharCode((bits & 0xFF00) >> 8);
        }
        if ((bits & 0xFF) > 0) {
            decoded += String.fromCharCode(bits & 0xFF);
        }
    }
    return decoded;
}

// Test.assertEquals('Man'.toBase64(), 'TWFu');
// Test.assertEquals('TWFu'.fromBase64(), 'Man');

// Test.assertEquals('M'.toBase64(), 'TQ==');
// Test.assertEquals('TQ=='.fromBase64(), 'M');

// Test.assertEquals('Ma'.toBase64(), 'TWE=');
// Test.assertEquals('TWE='.fromBase64(), 'Ma');

// Test.assertEquals('this is a string!!'.toBase64(), 'dGhpcyBpcyBhIHN0cmluZyEh');
// Test.assertEquals('dGhpcyBpcyBhIHN0cmluZyEh'.fromBase64(), 'this is a string!!');

// var text = 'Man is distinguished, not only by his reason, but by this singular passion from ' +
// 'other animals, which is a lust of the mind, that by a perseverance of delight ' +
// 'in the continued and indefatigable generation of knowledge, exceeds the short ' +
// 'vehemence of any carnal pleasure.';
// console.log(text.toBase64());



function PrimeFactorizer(n) {
    var factors = {};

    var _isPrime = function (n) {
        if (n == 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        var root = Math.floor(Math.sqrt(n));
        var isPrime = true;
        for (var i = 3; i < root && isPrime; i += 2) {
            if (n % i == 0)
                isPrime = false;
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
        console.log(n);
        if (_isPrime(n)) {
            factors[n.toString()] = 1;
        }
        else {

            var primes = _generatePrimes(Math.sqrt(n));
            var rest = n;
            for (var i = 0; i < primes.length && rest > 1; i++) {
                while (rest % primes[i] == 0 && rest > 1) {
                    factors[primes[i].toString()] = (factors[primes[i].toString()] || 0) + 1;
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

// console.log(new PrimeFactorizer(24).factor);
// console.log(new PrimeFactorizer(10967535067).factor);

function isMerge(s, part1, part2) {
    console.log("In: ", s);
    console.log("P1: ", part1);
    console.log("P2: ", part2);

				if (s.length != part1.length + part2.length)
        return false;
				for (var i = 0; i < s.length; i++) {
        if (s.charAt(i) == part1.charAt(0))
            part1 = part1.slice(1);
        else if (s.charAt(i) == part2.charAt(0))
            part2 = part2.slice(1);
        else
            return false;
				}
    return true;
}

// Test.expect(isMerge('codewars', 'code', 'wars'));
// Test.expect(isMerge('codewars', 'cdw', 'oears'));
// Test.expect(!isMerge('codewars', 'cod', 'wars'));
// Test.expect(isMerge('Bananas from Bahamas', 'Bahas', 'Bananas from am'));

String.prototype.asInt = function() {
    return this.charCodeAt(0) - 48;
};

Number.prototype.asStr = function() {
    return String.fromCharCode(this + 48);
};

var add = function (a, b) {
    var ar = a.split('');
    var br = b.split('');
    var carry = 0;
    var sum = [];
    var v1 = ar.pop();
    var v2 = br.pop();
    for(; v1 || v2; v1 = ar.pop(), v2 = br.pop()) {
        var s = carry + (v1 || '0').asInt() + (v2 || '0').asInt();
        carry = (s & 2) >> 1;
        sum.unshift((s & 1).asStr());
    }
    if(carry === 1) {
        sum.unshift('1');
    }
    return sum.join('');
    // var ar = a.split('').reverse();
    // var br = b.split('').reverse();
    // var carry = 0;
    // var sum = [];
    // for (var i = 0; i < Math.max(ar.length, br.length); i++) {
    //     var s = carry + (ar[i] || '0').asInt() + (br[i] || '0').asInt();
    //     carry = (s & 2) >> 1;
    //     sum.push((s & 1).asStr());
    // }
    // if(carry == 1) {
    //     sum.push(carry.asStr());
    // }
    // return sum.reverse().splice(sum.findIndex(function(z) { return z === '1'; })).join('');
}

// Test.assertEquals(add('111', '10'), '1001');
// Test.assertEquals(add('1101', '101'), '10010');
// Test.assertEquals(add('1101', '10111'), '100100');

var fibs = [];
var fib = function(prod) {
    var fibProd = 0;
    var ret = [0, 1, false];
    var fib = 0;
    var n1 = 0;
    var n2 = 1;
    while(true) {
        fib = ret[0] + ret[1];
        ret[0] = ret[1];
        ret[1] = fib;
        fibProd = ret[0] * ret[1];
        ret[2] = fibProd === prod;
        if(fibProd >= prod) break;
    }
    return ret;
}

console.log(fib(84049690));
