describe("primes", function() {
    it("calculates primes to n", function() {
        expect(1).toBePrime();
        expect(2).toBePrime();
        expect(3).toBePrime();
        expect(4).not.toBePrime();
        expect(5).toBePrime();
        expect(6).not.toBePrime();
        expect(7).toBePrime();
        expect(8).not.toBePrime();
        expect(9).not.toBePrime();
        expect(10).not.toBePrime();
        expect(25).not.toBePrime();
        expect(27).not.toBePrime();
        expect(29).toBePrime();
        expect(30).not.toBePrime();
        expect(31).toBePrime();
    });
});

