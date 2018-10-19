var eles = document.getElementsByTagName("code");
var max = eles.length;
console.log(max);
for (var i=0; i<max; i++) {
  if (eles[i].parentNode.tagName == "PRE") {
    eles[i].setAttribute("id", "_code" + i)
    var btn = document.createElement("div");
    btn.className = "btn-copy"; 
    btn.setAttribute("data-clipboard-target", "#_code" + i);
    btn.setAttribute("data-interactive", true);
    eles[i].parentNode.prepend(btn);
  }
};
var clipboard = new ClipboardJS('.btn-copy');
clipboard.on('success', function(e) {
  console.log(e);
  document.getElementById("topmsg").style.opacity = 1;
  setTimeout(function() {
    document.getElementById("topmsg").style.opacity = 0;
  }, 500);
  e.clearSelection();
});
clipboard.on('error', function(e) {
  console.log(e);
});
