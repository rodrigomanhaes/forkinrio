describe("rational numbers", function() {
    it("sums", function() {
        r1 = new Rational(1, 3);
        r2 = new Rational(2, 5);
        expect(r1.add(r2)).toEqual(new Rational(11, 15));
    });

    it("subtracts", function() {
        r1 = new Rational(2, 5);
        r2 = new Rational(1, 3);
        expect(r1.subtract(r2)).toEqual(new Rational(1, 15));
    });

    it("multiplies", function() {
        r1 = new Rational(2, 5);
        r2 = new Rational(1, 3);
        expect(r1.multiply(r2)).toEqual(new Rational(2, 15));
    });

    it("divides", function() {
        r1 = new Rational(2, 5);
        r2 = new Rational(1, 3);
        expect(r1.divide(r2)).toEqual(new Rational(6, 5));
    });
});

