//Create a table of Project Euler solutions and display it on the article
//Plus, I don't want to spend a lot of writing all the links one by one.

function generate_solutions()
{
	var rows = 51;

	var table = document.getElementById("pe_solutions");
	
	for(var i=0; i<rows; i++)
	{
		var row = table.insertRow(i);
		var cellA = row.insertCell(0);
		var cellB = row.insertCell(1);

		var github_link = "https://www.github.com/MegaColorBoy/ProjectEuler/blob/master/p{num}.py";
		var probLink = "https://projecteuler.net/problem=" + (i+1);
		var solLink = ((i+1) < 9) ? github_link.replace("{num}", "0"+(i+1)) : github_link.replace("{num}", ""+(i+1));
		
		cellA.innerHTML = `<a href="` + probLink + `">Problem ` + (i+1) + `</a>`;
		cellB.innerHTML = `<a href="` + solLink + `">Solution ` + (i+1) + `</a>`;
	}
}

generate_solutions();