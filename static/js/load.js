window.onload = function() {
    setTimeout(function() {

        var tag = document.getElementsByTagName("span")[0];
        var id = tag.dataset.id;
        
        var wait_screen = document.getElementById("wait");
        wait_screen.style.display = "none"
        var btn = document.getElementById('clickbtn');
        btn.style.display = "inline-block";
    }, 3000)
}