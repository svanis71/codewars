import { arrayStringPrototype } from '../kyu6/array_toString';

Array.prototype.toString = arrayStringPrototype;


test('[1,2]', () => {
    expect([1,2].toString()).toBe('[1,2]');
});

test('[true,false]', () => {
    expect([true,false].toString()).toBe('[true,false]');
});

test('[1,[2]]', () => {
    expect([1,[2]].toString()).toBe('[1,[2]]');
});

test('[1,"2"]', () => {
    expect([1,'2'].toString()).toBe('[1,\'2\']');
});

test('[]', () => {
    expect([].toString()).toBe('[]');
});