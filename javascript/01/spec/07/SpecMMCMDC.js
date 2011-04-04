describe("MMC e MDC", function() {
    it("mmc", function() {
        expect((2).mmc(3)).toEqual(6);
        expect((3).mmc(2)).toEqual(6);
        expect((4).mmc(6)).toEqual(12);
        expect((3).mmc(9)).toEqual(9);
        expect((6).mmc(8)).toEqual(24);
    });

    it("mdc", function() {
        expect((6).mdc(4)).toEqual(2);
        expect((18).mdc(12)).toEqual(6);
        expect((100).mdc(75)).toEqual(25);
    });
});

