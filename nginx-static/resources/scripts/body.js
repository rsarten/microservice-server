function myFunction(elmnt,clr) {
    elmnt.style.color = clr;
}

function getNews() {
	fetch("http://128.199.176.124/flask")
	.then(function(response) {
		if (response.ok) {response.json()
		.then(function(data) {alert(JSON.stringify(data)); });
		} else { alert('no luck!');
		}
	}, function(e) { alert('error!', e);
	//document.getElementById('main-body').innerHTML = JSON.stringify(response);
	});
}
//fetch("http://localhost/flask").then(function(response) { return response.text(); }).then(function(response) {console.log(response); });
