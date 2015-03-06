f :: [Int] -> Int
f arr = (foldr (+) 0 [x | x <- arr, x `mod` 2 == 1])


-- This part handles the Input/Output and can be used as it is. Do not change or modify it.
main = do
   inputdata <- getContents
   putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata