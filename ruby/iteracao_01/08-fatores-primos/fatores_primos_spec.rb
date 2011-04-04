require File.join(File.dirname(__FILE__), 'fatores_primos')

describe Integer do
  it 'calcula seus fatores primos' do
    630.fatores_primos.should == [2, 3, 3, 5, 7]
  end
end

