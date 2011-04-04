Number.prototype.multiple = function(n) {
    return this % n == 0;
}

Number.prototype.ricksSum = function() {
    var sum = 0, i;
    for (i = 0; i < this; i++)
        if (i.multiple(3) || i.multiple(5))
            sum += i;
    return sum;
};

