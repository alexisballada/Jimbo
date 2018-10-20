function fetchContent() {
    $("#questions").load('new_ques.php');
    

    window.setTimeout(fetchContent, 1000);
}

$(document).ready(function(){
    var colors = ["FFD4D3", "8AD2A2", "FE8783"];

    $("#symptoms").keyup(function(e){
        if(e.keyCode == 13) {


            var textToSave = document.getElementById("symptoms").value
            var index = Math.floor(Math.random() * 3)

            $( "#wrapper" ).animate({
                backgroundColor: "#" + colors[index]
            }, 2000);

            $("#questions").fadeOut('slow', function(e) {
                $(fetchContent);
                
            });
            $("#questions").fadeIn(1000);

        }
    }
)});