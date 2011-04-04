Number.prototype.mmc = function(other) {
    var mmcWannabe = this > other ? this : other;
    while (true) {
        if (mmcWannabe.multiple(this) && mmcWannabe.multiple(other))
            return mmcWannabe;
        mmcWannabe++;
    }
};

Number.prototype.mdc = function(other) {
    var mdcWannabe = this < other ? this : other;
    while (true) {
        if (this.multiple(mdcWannabe) && other.multiple(mdcWannabe))
            return mdcWannabe;
        mdcWannabe--;
    }
}

