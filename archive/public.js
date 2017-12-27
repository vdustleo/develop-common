var m=10;
//alert("I am public.js");
window.onload=function(){
	//alert("loaded!");
	//alert("loaded!sss");
	
	var x = document.getElementsByTagName("h1")[0];
	var y = document.getElementsByTagName("p")[0];
	//x.parentNode.insertBefore(y,x);
	//x.parentNode.appendChild(x);
	//var z = x.removeChild(y);
	//y.parentNode.appendChild(z);
	//var y = x.firstChild;
	//var z =  document.getElementsByTagName("p")[1];
	//z.appendChild(y);
	
	var j = document.createElement('p');
	var k = document.createTextNode('This is a test!');
	j.appendChild(k);
	j.onclick=function(){
		//alert("you click a <p>!");
	};
	document.body.appendChild(j);
	
	document.body.appendChild(j.cloneNode(true));
	document.body.appendChild(j.cloneNode(true));
	};
	

