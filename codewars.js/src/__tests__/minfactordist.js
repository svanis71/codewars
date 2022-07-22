import { minDistance } from '../minfactordist';

test("should pass sample tests", function() {
    expect(minDistance(8)).toEqual(1);
    expect(minDistance(25)).toEqual(4);
    expect(minDistance(13013)).toEqual(2);
    expect(minDistance(218683)).toEqual(198);
  });