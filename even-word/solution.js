function solution(S) {
	if (S.length === 0 || S.length > 200000) {
		return 0;
	}

	const lowerCase = S.toLowerCase();

	// create a variable to track number of deleted letters
	// create an object to keep track of the total occurences of a letter

	let deletedLettersCount = 0;
	let countOfLetters = {};

	for (let letter of lowerCase) {
		if (countOfLetters[letter]) {
			countOfLetters[letter]++;
		} else {
			countOfLetters[letter] = 1;
		}
	}

	console.log(countOfLetters);

	// check for odd elements
	// loop through the object and look for odd numbers

	for (let letter in countOfLetters) {
		if (countOfLetters[letter] % 2 !== 0) {
			deletedLettersCount++;
		}
	}

	return deletedLettersCount;
}

console.log(solution('acbcbba'));
console.log(solution('axxaxa'));
console.log(solution('aaaa'));
console.log(solution('zzbbxxxcccd'));

// to check for letters a-z -> regex
