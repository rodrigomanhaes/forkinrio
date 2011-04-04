# coding: utf-8

require File.join(File.dirname(__FILE__), 'prime')

print 'Enter a number: '
number = gets.to_i

primes = (1..number).select {|n| n.prime? }
puts "Prime numbers between 1 and #{number}:\n  #{primes.join(', ')}"

