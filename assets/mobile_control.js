var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
console.log(width);
if (width <= 600) {
  document.getElementById("light-twitter-timeline").style.display = "none";
  document.getElementById("dark-twitter-timeline").style.display = "none";
}