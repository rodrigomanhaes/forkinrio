describe("Number", function() {
    it("happy?", function() {
        expect(1).toBeHappy();
        expect(7).toBeHappy();
        expect(10).toBeHappy();
        expect(13).toBeHappy();
        expect(19).toBeHappy();
        expect(392).toBeHappy();
        expect(490).toBeHappy();
        expect(2).not.toBeHappy();
        expect(15).not.toBeHappy();
        expect(92).not.toBeHappy();
        expect(387).not.toBeHappy();
        expect(495).not.toBeHappy();
    });
});

