# coding: utf-8

class Cliente
  attr_reader :codigo, :altura, :peso

  def initialize(codigo, altura, peso)
    @codigo, @altura, @peso = codigo, altura, peso
  end

  def to_s
    "Código: %d, altura: %.2fm, peso: %.1fkgf" % [codigo, altura, peso]
  end
end

class Array
  def average(&block)
    map(&block).reduce {|a, b| a + b } / count
  end
end

clientes = []
begin
  puts 'Dados do cliente'
  print 'Código: '
  codigo = gets.to_i
  if codigo != 0
    print 'Altura (m): '
    altura = gets.to_f
    print 'Peso (kgf): '
    peso = gets.to_f
    clientes << Cliente.new(codigo, altura, peso)
  end
end until codigo.zero?

puts "Mais alto: %s" % clientes.max_by(&:altura)
puts "Mais baixo: %s" % clientes.min_by(&:altura)
puts "Altura média: %.2fm" % clientes.average(&:altura)

puts "Mais gordo: %s" % clientes.max_by(&:peso)
puts "Mais magro: %s" % clientes.min_by(&:peso)
puts "Peso médio: %.1fkgf" % clientes.average(&:peso)

