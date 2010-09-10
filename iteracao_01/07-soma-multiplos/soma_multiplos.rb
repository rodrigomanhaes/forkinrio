puts (1..9).
  select {|n| n % 3 == 0 || n % 5 == 0 }.
  reduce {|a, b| a + b }

