Madison

A simple scripting language built onto python.

Run with: 
$ python parse.py

Examples:
	
	madison> let;five;5
	five means 5
	madison> five
	5
	madison> let;three;3
	three means 3
	madison> do;print(five*three);4
	15
	15
	15
	15
	madison> let;three;5
	You told me "three" meant 3 - did you lie?
	madison> three
	3
	madison> let;7;1
	"7" is not a sequence of letters!


Above examples in one command:

	madison> let;three;3;;let;three;3;;do;print(five*three);4;;let;three;5;;three;;let;7;1
	five means 5
	5
	three means 3
	15
	15
	15
	15
	You told me "three" meant 3 - did you lie?
	3
	"7" is not a sequence of letters!

Lists work as well:

	madison> let;first;list([1, 2, 3])
	first means [1, 2, 3]
	madison> let;second;list([4, 5, 6])
	second means [4, 5, 6]
	madison> let;third;list([7, 8, 9])
	third means [7, 8, 9]
	madison> let;threeByThree;list([first, second, third])
	threeByThree means [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	madison> let;firstS;list(["a", "b", "c"])
	firstS means ["a", "b", "c"]
	madison> let;secondS;list(["d", "e", "f"])
	secondS means ["d", "e", "f"]
	madison> let;thirdS;list([["g", "h", "i"])
	thirdS means ["g", "h", "i"]
	madison> let;threeByThreeS;list([firstS, secondS, thirdS])
	threeByThreeS means [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]