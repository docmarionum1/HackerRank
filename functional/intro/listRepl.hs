import Data.List

f :: Int -> [Int] -> [Int]
f n arr = concat [replicate n x | x <- arr]

main :: IO ()
main = getContents >>=
       mapM_ print. (\(n:arr) -> f n arr). map read. words