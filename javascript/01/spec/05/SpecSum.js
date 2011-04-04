describe("soma ricks", function() {
    it("sums all numbers lower than itself that are multiple of 3 or 5", function() {
        expect((0).ricksSum()).toEqual(0);
        expect((1).ricksSum()).toEqual(0);
        expect((2).ricksSum()).toEqual(0);
        expect((3).ricksSum()).toEqual(0);
        expect((4).ricksSum()).toEqual(3);
        expect((5).ricksSum()).toEqual(3);
        expect((6).ricksSum()).toEqual(8);
        expect((7).ricksSum()).toEqual(14);
        expect((8).ricksSum()).toEqual(14);
        expect((9).ricksSum()).toEqual(14);
        expect((10).ricksSum()).toEqual(23);
        expect((11).ricksSum()).toEqual(33);
        expect((12).ricksSum()).toEqual(33);
        expect((13).ricksSum()).toEqual(45);
    });
});

