

$(document).ready(function(){
    var colors = ["FFD4D3", "8AD2A2", "FE8783"];
    var inputs = []

    $("#symptoms").keyup(function(e){
        if(e.keyCode == 13) {
            inputs.push(document.getElementById("symptoms").value);
            var index = Math.floor(Math.random() * 3)
            $( "#wrapper" ).animate({
                backgroundColor: "#" + colors[index]
            }, 2000);
            $("#questions").fadeOut('slow', function(e) {
                //Call to evaluation script w/ inputs[]
                //change inner HTML to next question
                document.getElementById("questions").innerHTML = "That's good to hear."
            });
            $("#questions").fadeIn(1000);

        }
    }
)});