Array.prototype.contains = function(elem) {
    for (i = 0; i < this.length; i++)
        if (elem == this[i])
            return true;
    return false;
}

Number.prototype.square = function() {
    return this * this;
};

Number.prototype.isHappy = function() {
    var number = this;
    var numbers = [];
    while (!numbers.contains(number) && number != 1) {
        numbers.push(number);
        s = "" + number;
        number = 0;
        for (i = 0; i < s.length; i++)
            number += parseInt(s.charAt(i)).square();

    }
    return number == 1;
}

