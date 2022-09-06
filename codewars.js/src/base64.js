export function toBase64() {
  var base64Table =
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
  var charCodes = this.split('').map(function (c) {
    return c.charCodeAt(0);
  });
  var encodedString = '';

  for (var i = 0; i < charCodes.length; i += 3) {
    var base64Code =
      (charCodes[i] << 16) |
      (charCodes[i + 1] << 8 || 0) |
      (charCodes[i + 2] || 0);
    encodedString += base64Table[(base64Code & 0xfc0000) >> 18];
    encodedString += base64Table[(base64Code & 0x03f000) >> 12];
    if (i + 1 < charCodes.length) {
      encodedString += base64Table[(base64Code & 0x000fc0) >> 6];
      if (i + 2 < charCodes.length) {
        encodedString += base64Table[base64Code & 0x3f];
      } else {
        encodedString += '=';
      }
    } else {
      encodedString += '==';
    }
  }
  return encodedString;
}

export function fromBase64() {
  var base64Table =
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
  var encodedValues = this.split('').map(function (s1) {
    if (s1 != '=') {
      return base64Table.indexOf(s1);
    }
    return 0;
  });
  var decoded = '';

  for (var i = 0; i < encodedValues.length; i += 4) {
    var bits = encodedValues[i] << 18;
    bits |= (encodedValues[i + 1] || 0) << 12;
    bits |= (encodedValues[i + 2] || 0) << 6;
    bits |= encodedValues[i + 3] || 0;
    decoded += String.fromCharCode((bits & 0xff0000) >> 16);
    if ((bits & 0xff00) > 0) {
      decoded += String.fromCharCode((bits & 0xff00) >> 8);
    }
    if ((bits & 0xff) > 0) {
      decoded += String.fromCharCode(bits & 0xff);
    }
  }
  return decoded;
}
