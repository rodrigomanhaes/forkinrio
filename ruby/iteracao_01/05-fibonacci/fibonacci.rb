class Integer
  def fibonacci_set
    fibset = [1, 1]
    return fibset[0..self-1] if self <= 2
    (3..self).each { fibset << fibset[-1] + fibset[-2] }
    fibset
  end
end

