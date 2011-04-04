class Integer
  def mmc(other)
    mmc = nil
    count = [self, other].min
    while !mmc
      mmc = count if count % self == 0 && count % other == 0
      count += 1
    end
    mmc
  end

  def mdc(other)
    mdc = nil
    count = [self, other].min
    while !mdc
      mdc = count if self % count == 0 && other % count == 0
      count -= 1
    end
    mdc
  end
end

