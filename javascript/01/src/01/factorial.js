Number.prototype.loopFactorial = function() {
    ac = 1
    for (i = 1; i <= this; i++)
      ac *= i;
    return ac;
};

Number.prototype.recursiveFactorial = function() {
    if (this == 0)
        return 1;
    return this * (this - 1).recursiveFactorial();
};

