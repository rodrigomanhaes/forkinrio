# coding: utf-8

require File.join(File.dirname(__FILE__), 'tabuada')

describe Integer do
  context 'deve calcular tabuada de multiplicacao' do
    it 'de 1 a 10 como padrão' do
      5.tabuada.should == {1 => 5, 2 => 10, 3 => 15, 4 => 20, 5 => 25,
                           6 => 30, 7 => 35, 8 => 40, 9 => 45, 10 => 50}
    end

    it 'com inicio e fim determinados' do
      5.tabuada(4..9).should == {
        4 => 20, 5 => 25, 6 => 30, 7 => 35, 8 => 40, 9 => 45}
    end
  end
end

