describe("factorial", function() {
    it("basic algorithm class way", function() {
        expect((0).loopFactorial()).toEqual(1);
        expect((1).loopFactorial()).toEqual(1);
        expect((2).loopFactorial()).toEqual(2);
        expect((3).loopFactorial()).toEqual(6);
        expect((4).loopFactorial()).toEqual(24);
        expect((5).loopFactorial()).toEqual(120);
        expect((6).loopFactorial()).toEqual(720);
    });

    it("recursive way", function() {
        expect((0).recursiveFactorial()).toEqual(1);
        expect((1).recursiveFactorial()).toEqual(1);
        expect((2).recursiveFactorial()).toEqual(2);
        expect((3).recursiveFactorial()).toEqual(6);
        expect((4).recursiveFactorial()).toEqual(24);
        expect((5).recursiveFactorial()).toEqual(120);
        expect((6).recursiveFactorial()).toEqual(720);
    });
});

