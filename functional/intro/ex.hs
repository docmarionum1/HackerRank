solve :: Double -> Double
solve x = 1 + (foldr (+) 0 [x**i / product [1..i] | i <- [1..9]])

main :: IO ()
main = getContents >>= mapM_ print. map solve. map (read::String->Double). tail. words