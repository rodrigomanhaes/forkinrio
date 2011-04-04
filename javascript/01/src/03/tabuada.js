Number.prototype.tabuada = function() {
    var i;
    var result = [];
    var start = 0, end = 10;
    if (arguments.length == 2) {
        start = arguments[0];
        end = arguments[1];
    }
    for (i = start; i <= end; i++)
        result.push(this + " x " + i + " = " + (this * i));
    return result;
};

