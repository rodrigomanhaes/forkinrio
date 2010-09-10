class Fixnum
  def prime?
    (2..self/2).
      map {|n| self % n == 0 }.
      reject {|value| !value }.
      empty?
  end
end

