class Integer
  def tabuada(range = 1..10)
    result = {}
    range.each {|n| result[n] = self * n }
    result
  end
end

