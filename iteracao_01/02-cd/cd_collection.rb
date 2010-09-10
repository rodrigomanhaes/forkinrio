# coding: utf-8

print 'Quantidade de CDs: '
quantidade = gets.to_i

total = 0.0
quantidade.times do |n|
  print "Valor do CD ##{n+1}: "
  total += gets.to_f
end

puts "Valor total da coleção: #{total}"
puts "Valor médio de cada CD: #{total/quantidade}"

