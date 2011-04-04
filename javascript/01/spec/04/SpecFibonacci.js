describe("fibonacci", function() {
    it("generates the selfth first members of fibonacci set", function() {
        expect((1).fibonacciSet()).toEqual([1]);
        expect((2).fibonacciSet()).toEqual([1, 1]);
        expect((3).fibonacciSet()).toEqual([1, 1, 2]);
        expect((4).fibonacciSet()).toEqual([1, 1, 2, 3]);
        expect((5).fibonacciSet()).toEqual([1, 1, 2, 3, 5]);
        expect((6).fibonacciSet()).toEqual([1, 1, 2, 3, 5, 8]);
        expect((7).fibonacciSet()).toEqual([1, 1, 2, 3, 5, 8, 13]);
        expect((8).fibonacciSet()).toEqual([1, 1, 2, 3, 5, 8, 13, 21]);
        expect((9).fibonacciSet()).toEqual([1, 1, 2, 3, 5, 8, 13, 21, 34]);
        expect((10).fibonacciSet()).toEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]);
    });
});

