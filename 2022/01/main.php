<!doctype html>
<html>
	<? $aoc_d1 = "AoC 2022 - Day 01" ?>
	
	<head>
		<title><?= $aoc_d1 ?></title>
		<style>
			pre {
				background-color: #eee;
				border: 1px #ddd solid;
				border-radius: 5px;
				padding: 3px 5px;
			}
		</style>
	</head>
	
	<body>
		<h1><?= $aoc_d1 ?></h1>
		
		<?php
			$dataSource = $_GET["dataSource"];
			switch ($dataSource)
			{
				case "exampleData":
				case "inputData":
					break;
				default:
					$dataSource = "exampleData";
			}
			$dataFile = str_replace("Data", "", $dataSource).".txt";
		?>
		
		<form name="settings">
			<select name="dataSource">
				<option value="exampleData" <? if ($dataSource === "exampleData"): ?>selected<? endif; ?>>example data</option>
				<option value="inputData" <? if ($dataSource === "inputData"): ?>selected<? endif; ?>>input data</option>
			</select>
			<button submit>submit</button>
		</form>
		
		<?php
function getTotalCalories()
{
	$totalCalories = array();
	$calories = 0;
	
	// open file
	$fileHandle = fopen($GLOBALS["dataFile"], "r");

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
	$totalCalories = getTotalCalories();
	
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
		<p><? main($dataSource); ?></p>
		
		<h2>JavaScript</h2>
		<p id="resultsParagraph">placeholder</p>
		
		<details>
			<summary>
				<? if ($dataSource === "exampleData"): ?>
					Example data
				<? elseif ($dataSource === "inputData"): ?>
					My input data
				<? endif; ?>
			</summary>
			<pre id="<?= $dataSource ?>"><?= file_get_contents($dataFile); ?></pre>
		</details>
		
		<script>
			<? include("main.js") ?>
			main("<?= $dataSource ?>");
		</script>
	</body>
</html>