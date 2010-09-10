class Fixnum
  def prime?
    (2..self/2).
      select {|n| self % n == 0 }.
      empty?
  end
end

