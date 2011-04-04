# coding: utf-8

require File.join(File.dirname(__FILE__), 'tabuada')

print 'Montar a tabuada de: '
numero = gets.to_i
print 'Começar em: '
inicio = gets.to_i
print 'Terminar em: '
fim = gets.to_i

puts "Vou montar a tabuada de %d começando em %d e terminando em %d" %
  [numero, inicio, fim]
resultado = numero.tabuada(inicio..fim)
resultado.each_pair do |mult, result|
  puts "%d * %d = %s" % [numero, mult, result]
end

