import { shapeArea } from '../kyu7/shape_area';

test('Test 1', () => {
    expect(shapeArea(1)).toBe(1);
});
test('Test 2', () => {
    expect(shapeArea(2)).toBe(5);
});
test('Test 3', () => {
    expect(shapeArea(3)).toBe(13);
});
test('Test 4', () => {
    expect(shapeArea(3)).toBe(13);
});
test('Test 5', () => {
    expect(shapeArea(5)).toBe(41);
});