import { sortByArea } from '../kyu7/sort_circle_rect_area';

test('Basic', function() {
    expect(sortByArea([[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]])).toEqual([4.31, 4.75, 27.2, 37.26]);
    expect(sortByArea([1.23])).toEqual([4.75]);
    expect(sortByArea([[2.345, 5.6765]])).toEqual([13.31]);
    expect(sortByArea([[2, 5], 6])).toEqual([10, 113.1]);
    });