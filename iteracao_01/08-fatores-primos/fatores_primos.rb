require File.expand_path(File.join(File.dirname(__FILE__), '../03-primos/prime'))

class Integer
  def fatores_primos
    fatores_primos = []
    quociente = self
    begin
      mdp = quociente.menor_divisor_primo
      fatores_primos << mdp
      quociente = quociente / mdp
    end until quociente == 1
    fatores_primos
  end

  def menor_divisor_primo
    return self if self < 2
    (2..self/2).each {|n| return n if self % n == 0 && n.prime? }
    return self
  end
end

