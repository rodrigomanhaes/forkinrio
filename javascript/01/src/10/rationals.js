Rational = function(numerator, denominator) {
    this.numerator = numerator;
    this.denominator = denominator;
}

Rational.prototype.add = function(other) {
    result_denominator = this.denominator.mmc(other.denominator);
    return new Rational(
        (result_denominator / this.denominator * this.numerator) +
        (result_denominator / other.denominator * other.numerator),
        result_denominator);
};

Rational.prototype.inverse = function() {
    return new Rational(-this.numerator, this.denominator);
};

Rational.prototype.subtract = function(other) {
    return this.add(other.inverse());
};

Rational.prototype.multiply = function(other) {
    return new Rational(this.numerator * other.numerator,
                         this.denominator * other.denominator);
};

Rational.prototype.divide = function(other) {
    return new Rational(this.numerator * other.denominator,
                         this.denominator * other.numerator);
};

