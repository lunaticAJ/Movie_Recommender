function content(e,n) {
  localStorage.setItem('title', e.getAttribute('title'));
  localStorage.setItem('classifier', n);
  window.document.location="recommend?movie="+e.getAttribute('title')+"&classifier="+n;
	document.getElementById("block").style.height = '50%';
	document.querySelector("#loader").style.display = "block";
}