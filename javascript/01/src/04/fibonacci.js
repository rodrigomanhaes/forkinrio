Number.prototype.fibonacciSet = function() {
    if (this == 1)
        return [1];
    if (this == 2)
        return [1, 1];
    var set = [1, 1]
    var i
    var last1 = 1
    var last2 = 1
    for (i = 3; i <= this; i++) {
        var current = last1 + last2
        set.push(current)
        last2 = last1
        last1 = current;
    }
    return set;
};

