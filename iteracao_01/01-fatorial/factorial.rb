class Fixnum
  def classical_factorial
    return 1 if zero?
    self * (self - 1).classical_factorial
  end

  def non_recursive_pascal_like_factorial
    return 1 if zero?
    result = 1
    for n in 2..self
      result *= n
    end
    result
  end

  def idiomatic_factorial
    return 1 if zero?
    (1..self).reduce {|a, b| a * b }
  end
end

