<!doctype html>
<html>
	<? $aoc_d1 = "AoC 2022 - Day 01"; ?>
	
	<head>
		<title><?= $aoc_d1 ?></title>
		<script src="main.js" defer></script>
		<style>
			pre {
				background-color: #eee;
				border: 1px #ddd solid;
				border-radius: 5px;
				padding: 3px 5px;
			}
		</style>
	</head>
	
	<body onload="main();">
		<h1><?= $aoc_d1 ?></h1>
		
		<form>
			<select>
				<option></option>
			</select>
		</form>
		
		<?php
function getTotalCalories($filename)
{
	$totalCalories = array();
	$calories = 0;
	
	// open file
	$fileHandle = fopen($filename, "r");

	// read line by line
	while ($line = fgets($fileHandle))
	{
		if ($line === "\r\n")
		{
			$totalCalories[] = $calories;
			$calories = 0;
		}
		else
		{
			$calories += (int)$line;
		}
	}
	$totalCalories[] = $calories;
	
	// sort ascending
	sort($totalCalories, SORT_NUMERIC);
	
	return $totalCalories;
}

function main()
{
	// get calories per elve
	// $totalCalories = getTotalCalories("example.txt");
	$totalCalories = getTotalCalories("input.txt");
	
	// get max calories
	$maxCalories = array_slice($totalCalories, count($totalCalories)-1);
	// get top 3 calories
	$top3Calories = array_slice($totalCalories, count($totalCalories)-3);
	
	// results
	echo("Part 1: ".array_sum($maxCalories)."<br>");
	echo("Part 2: ".array_sum($top3Calories));
}
		?>
		
		<h2>PHP</h2>
		<p><? main(); ?></p>
		
		<h2>JavaScript</h2>
		<p id="resultsParagraph"></p>
		
		<details open>
			<summary>Example data</summary>
			<pre id="exampleData"><?= file_get_contents("example.txt"); ?></pre>
		</details>
		<br>
		<details>
			<summary>My input data</summary>
			<pre id="inputData"><?= file_get_contents("input.txt"); ?></pre>
		</details>
	</body>
</html>