import Text.Printf (printf)

fun :: [Int] -> [Int] -> Double -> Double
fun a b x = (foldr (+) 0.0 [fromIntegral (a!!i) * (x**fromIntegral(b!!i)) | i <- [0..(length a)-1]])

-- This function should return a list [area, volume].
solve :: Double -> Double -> [Int] -> [Int] -> [Double]
solve l r a b = ([	(foldr (+) 0.0 [fun a b x | x <- [l,l + 0.001..r]]) / 1000,
					(foldr (+) 0.0 [pi*(fun a b x)**2 | x <- [l,l + 0.001..r]]) / 1000])

--Input/Output.
main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n"). (\[a, b, [l, r]] -> solve (fromIntegral l) (fromIntegral r) a b). map (map read. words). lines
