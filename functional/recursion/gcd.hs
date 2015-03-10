module Main where

gcd' :: Integral a => a -> a -> a
gcd' n m =
    if n == m then n else
    let a = max n m
        b = min n m
    in
        let c = a - b
            d = max b c
            e = min b c
        in
            gcd' d e
            

-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
  input <- getLine
  print . uncurry gcd' . listToTuple . convertToInt . words $ input
 where
  listToTuple (x:xs:_) = (x,xs)
  convertToInt = map (read :: String -> Int)