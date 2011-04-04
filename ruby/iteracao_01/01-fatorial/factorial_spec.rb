# coding: utf-8

require File.join(File.dirname(__FILE__), 'factorial')

describe Fixnum do
  def run_factorial(factorial_method)
    0.send(factorial_method).should == 1
    1.send(factorial_method).should == 1
    2.send(factorial_method).should == 2
    3.send(factorial_method).should == 6
    4.send(factorial_method).should == 24
    5.send(factorial_method).should == 120
    6.send(factorial_method).should == 720
    7.send(factorial_method).should == 5040
  end

  context 'should calculate its factorial' do
    it 'in a classical, recursive way' do
      run_factorial :classical_factorial
    end

    it 'in a pascal-like, boring way' do
      run_factorial :non_recursive_pascal_like_factorial
    end

    it 'in an idiomatic, cool functional rubyist way' do
      run_factorial :idiomatic_factorial
    end
  end
end

