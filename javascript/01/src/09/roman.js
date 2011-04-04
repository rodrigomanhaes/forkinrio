Number.prototype.floor = function() {
    return Math.floor(this);
}

Number.prototype.toRoman = function() {
    convert = function(num, one, five, ten) {
        switch(num) {
            case 1: return one;
            case 2: return one + one;
            case 3: return one + one + one;
            case 4: return one + five;
            case 5: return five;
            case 6: return five + one;
            case 7: return five + one + one;
            case 8: return five + one + one + one;
            case 9: return one + ten;
        }
        return "";
    };

    return convert((this / 1000).floor(), "M", "", "") +
            convert((this % 1000 / 100).floor(), "C", "D", "M") +
            convert((this % 1000 % 100 / 10).floor(), "X", "L", "C") +
            convert(this % 1000 % 100 % 10, "I", "V", "X");
}

