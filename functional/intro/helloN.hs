import Data.List

hello_worlds n = putStrLn (intercalate "\n" ["Hello World" | x <- [1..n]])

main = do
   n <- readLn :: IO Int
   hello_worlds n