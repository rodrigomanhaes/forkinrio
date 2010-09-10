# coding: utf-8

print 'Um número: '
numero = gets.to_i
print 'Outro número: '
outro = gets.to_i

require File.join(File.dirname(__FILE__), 'mdc_mmc')

[:mmc, :mdc].each { |op|
  puts "O %s entre %d e %d é %d" % [op.to_s.upcase, numero, outro, numero.send(op, outro)]
}

