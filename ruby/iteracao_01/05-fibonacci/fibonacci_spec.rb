require File.join(File.dirname(__FILE__), 'fibonacci')

describe Integer do
  it 'should generate the selfth first members of fibonacci set' do
    1.fibonacci_set.should == [1]
    2.fibonacci_set.should == [1, 1]
    3.fibonacci_set.should == [1, 1, 2]
    4.fibonacci_set.should == [1, 1, 2, 3]
    5.fibonacci_set.should == [1, 1, 2, 3, 5]
    6.fibonacci_set.should == [1, 1, 2, 3, 5, 8]
    7.fibonacci_set.should == [1, 1, 2, 3, 5, 8, 13]
    8.fibonacci_set.should == [1, 1, 2, 3, 5, 8, 13, 21]
    9.fibonacci_set.should == [1, 1, 2, 3, 5, 8, 13, 21, 34]
    10.fibonacci_set.should == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  end
end

