rev l = [l !! i | i <- [(length l) - 1,(length l) - 2..0]]


main = do
		inputdata <- getContents
		mapM_ putStrLn $ map show $ rev $ map (read :: String -> Int) $ lines inputdata