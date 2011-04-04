Number.prototype.is_prime = function() {
    var i
    for (i = 2; i <= this/2; i++)
        if (this % i == 0)
            return false;
    return true;
};

