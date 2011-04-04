beforeEach(function() {
  this.addMatchers({
    toBePrime: function() {
        return this.actual.is_prime();
    },
    toBeHappy: function() {
        return this.actual.isHappy();
    }
  })
});

