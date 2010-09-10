require File.join(File.dirname(__FILE__), 'prime')

describe Fixnum do
  it 'should respond if is a prime number' do
    1.should be_prime
    2.should be_prime
    3.should be_prime
    4.should_not be_prime
    5.should be_prime
    6.should_not be_prime
    7.should be_prime
    8.should_not be_prime
    9.should_not be_prime
    10.should_not be_prime
    11.should be_prime
    12.should_not be_prime
    13.should be_prime
    14.should_not be_prime
    15.should_not be_prime
  end
end

