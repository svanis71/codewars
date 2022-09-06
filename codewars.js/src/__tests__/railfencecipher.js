import { decodeRailFenceCipher, encodeRailFenceCipher } from '../railfencecipher';

describe('Encode', () => {
    test('Encode 1', () => {
        expect(encodeRailFenceCipher('WEAREDISCOVEREDFLEEATONCE', 3)).toEqual('WECRLTEERDSOEEFEAOCAIVDEN');
    });

    test('Encode 2', () => {
        expect(encodeRailFenceCipher('WEAREDISCOVEREDRUNATONCE', 6)).toEqual('WVOEOETNACRACRSENEEIDUDR');
    });
    
    test('Hello world', () => {
        expect(encodeRailFenceCipher('Hello, World!', 3)).toEqual('Hoo!el,Wrdl l');   
    });
});

describe('Decode', () => {

    test('Decode 1', () => {
        expect(decodeRailFenceCipher('WECRLTEERDSOEEFEAOCAIVDEN', 3)).toEqual('WEAREDISCOVEREDFLEEATONCE');
    });

    test('Decode 2', () => {
        expect(decodeRailFenceCipher('WVOEOETNACRACRSENEEIDUDR', 6)).toEqual('WEAREDISCOVEREDRUNATONCE');
    });

    test('Hello world', () => {
        expect(decodeRailFenceCipher('Hoo!el,Wrdl l', 3)).toEqual('Hello, World!');
    });
});
