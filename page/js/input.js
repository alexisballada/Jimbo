function input() {
    input = document.getElementById("symptoms").value;
    alert(input);

    //find out how to stick this input to karth's python code.
}

$(document).ready(function(){
    var colors = ["FFD4D3", "8AD2A2", "FE8783"];

    $("#symptoms").bind("enterKey", function(e){
        input();
        var index = Math.floor(Math.random() * 4)
        $( "#wrapper" ).animate({
            backgroundColor: "#" + colors[index]
        }, 1000);

    });
    $("#symptoms").keyup(function(e){
        if(e.keyCode == 13) {
            $(this).trigger("enterKey");
        }
    }

    

)});