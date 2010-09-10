require File.join(File.dirname(__FILE__), 'mdc_mmc')

describe Integer do
  it 'calcula o MMC entre si mesmo e outro inteiro' do
    1.mmc(2).should == 2
    2.mmc(5).should == 10
    3.mmc(6).should == 6
    4.mmc(6).should == 12
  end

  it 'calcula o MDC entre si mesmo e outro inteiro' do
    2.mdc(5).should == 1
    6.mdc(9).should == 3
    10.mdc(5).should == 5
    27.mdc(18).should == 9
  end
end

