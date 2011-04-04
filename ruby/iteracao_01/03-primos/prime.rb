class Fixnum
  def prime?
    (2..Math.sqrt(self).truncate).
      select {|n| self % n == 0 }.
      empty?
  end
end

