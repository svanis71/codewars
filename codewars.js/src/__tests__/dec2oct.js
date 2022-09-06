import { dec2Oct as f } from '../dec2octal_codegolf';

test('2', () => {
    expect(f('2')).toEqual(2);
});

test('16', () => {
    expect(f('8')).toEqual(10);
});