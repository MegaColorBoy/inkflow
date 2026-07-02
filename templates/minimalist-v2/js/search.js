// A mini search engine for the blog
var _url = "../json/til-posts.json";

function openSearch(){
	$("body").addClass("overlay");
	$(".tip, #closeSearch").show();
}

function closeSearch(resultsEl){
	$("body").removeClass("overlay");
	$(".tip, #closeSearch").hide();
	if(resultsEl){
		$(resultsEl).html('').hide();	
	}
}

$(document).ready(function(){

	var resultsEl = "#searchresults ul";
	
	$("#closeSearch").click(function(e){
		closeSearch(resultsEl);
	});

	$("#searchinput").focus(function(e){
		openSearch();
	// }).blur(function(e){
	// 	closeSearch(resultsEl);
	}).keyup(function(e){
		var code = e.keyCode ? e.keyCode : e.which;
		var keyword = $("#searchinput").val();
		var pattern = new RegExp(keyword, "gi");
		
		$(resultsEl).removeClass('no_results').html('');

		// Execute search if "Enter" key is pressed
		if(code == 13){
			$('.loader').show();				
			$.ajax({
				url: _url,
				type: "GET",
				dataType: "json",
				async: false,
				success: function(data) {
					// console.log('ok');
				}
			}).done(function(data){
				var results = "";
				if(data.posts.length > 0){
					$.each(data.posts, function(k,v){
						if(v.category.search(pattern) != -1 || v.title.search(pattern) != -1){
							
							// Highlight matched keyword
							var text = v.title.replace(pattern, function(keyword){
								return `<b>${keyword}</b>`
							});

							results += `<li onclick="window.location.href='../til/posts/${v.slug}'">
								<a>
									<span class="tag">${v.category}</span>${text}
								</a>
							</li>`;
						}
					});
				}

				if(results.length > 0){
					$(resultsEl).removeClass('no_results').html(results);
				}
				else {
					$(resultsEl).addClass('no_results').html(`<p style="margin:0;text-align:center;">No results matched.</p>`);
				}

				setTimeout(function(){
					$('.loader').hide();				
					$(resultsEl).show();
				}, 1000);
				
			});
		}
		else {
			$(resultsEl).hide();
		}
	});
});