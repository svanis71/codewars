require('../base64');

var tests = [
  ['this is a string!!', 'dGhpcyBpcyBhIHN0cmluZyEh'],
  ['this is a test!', 'dGhpcyBpcyBhIHRlc3Qh'],
  [
    'now is the time for all good men to come to the aid of their country.',
    'bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku',
  ],
  ['1234567890  ', 'MTIzNDU2Nzg5MCAg'],
  ['ABCDEFGHIJKLMNOPQRSTUVWXYZ ', 'QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog'],
  [
    'the quick brown fox jumps over the white fence. ',
    'dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g',
  ],
  [
    'dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4',
    'ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0',
  ],
  [
    'VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna',
    'VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h',
  ],
  ['TVRJek5EVTJOemc1TUNBZyAg', 'VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn'],
];

test('Test toBase64', () => {
  tests.forEach((testStr) => expect(testStr[0].toBase64()).toEqual(testStr[1]));
});

test('Test fromBase64', () => {
  tests.forEach((testStr) =>
    expect(testStr[1].fromBase64()).toEqual(testStr[0]),
  );
});
