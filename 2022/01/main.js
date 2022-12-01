function getTotalCalories(dataElement) {	
	let totalCalories = [];
	let calories = 0;
	
	// read line by line
	let data = document.getElementById(dataElement).innerHTML.split("\n");
	for (let i=0; i<data.length; i++) {
		line = data[i];
		if (line === "") {
			totalCalories.push(calories);
			calories = 0;
		}
		else {
			calories += Number(line);
		}
	}
	totalCalories.push(calories);
	
	// sort ascending
	totalCalories.sort((a, b) => a - b);
	
	return totalCalories;
}

function sum(array) {
	return array.reduce(function (accumVariable, curValue) {
		return accumVariable + curValue
	}, 0);
}

function main() {
	// get calories per elve
	// let totalCalories = getTotalCalories("exampleData");
	let totalCalories = getTotalCalories("inputData");
	
	// list length
	const tcLen = totalCalories.length
	// get max calories
	let maxCalories = totalCalories[tcLen-1];
	// get top 3 calories
	let top3Calories = [totalCalories[tcLen-1], totalCalories[tcLen-2], totalCalories[tcLen-3]];
	
	// results
	resultsElement = document.getElementById("resultsParagraph");
	resultsElement.innerHTML += "Part 1: " + maxCalories + "<br>";
	resultsElement.innerHTML += "Part 2: " + sum(top3Calories);
}
