// https://www.codewars.com/kata/58c5577d61aefcf3ff000081/solutions/javascript

const encode = (strng, numberRails) => {
    let dir = 1;
    let y = 0;
    const mat = [];
    for(let i = 0; i < numberRails; i++) {
        mat.push([]);
    }
    
    strng.split('').forEach(ch => {
        mat[y].push(ch);
        y += dir;
        if(y === 0 || y === numberRails - 1) {
          dir *= -1;
        }
    });
    return mat;
};

export function encodeRailFenceCipher(strng, numberRails) {

    return encode(strng, numberRails).reduce((a, b) => a.concat(b)).join('');
  }
  
export function decodeRailFenceCipher(encrypted, numberRails) {
    const splitSizes = encode(encrypted, numberRails).map(x => x.length);
    const encryptedChars = encrypted.split('');
    const parts = [];
    splitSizes.forEach(n => parts.push(encryptedChars.splice(0, n)));
    let y = 0;
    let dir = 1;
    let decrypted = '';
    for(let i = 0; i < encrypted.length; i++) {
        let ch = parts[y].splice(0, 1)[0];
        decrypted += ch;
        y += dir;
        if(y === 0 || y === numberRails - 1) {
          dir *= -1;
        }
    }
    return decrypted;
    // const repeatFreq = 2 * (N - 1);
    // const L = encrypted.length;
 
    // let x = 1;
    // let xtest = N;
    // while( N + ((N-1) * x) <= L) {
    //     x++;
    // }
    // xtest = N + ((N-1) * x);
    // const y = xtest - L;

    // // WVOEOETNACRACRSENEEIDUDR
    // const qq = (x+1)*(N-2);
    // const zz = ((L+y) - qq) / 2;

    // console.log(`qq=${qq} zz=${zz}`);
    // const enc = encrypted.split('')
    // const mat=[];
    // mat.push(enc.splice(0, zz));
    // for(let i=0; i < N-2; i++) {
    //     mat.push(enc.splice(0, x+1));
    // }
    // mat.push(enc);
    // console.log(mat);
    // // if(L % repeatFreq === 0) {
        
    // // }
    
    // // const K = L / repeatFreq;
    // // const start = enc.splice(0, K);
    // // const end = enc.splice(K);
    // return '';
  }