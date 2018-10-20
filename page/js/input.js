$(document).ready(function(){
    var colors = ["FFD4D3", "8AD2A2", "FE8783"];

    $("#symptoms").keyup(function(e){
        if(e.keyCode == 13) {

            var textToSave = document.getElementById("symptoms").value
            var index = Math.floor(Math.random() * 3)

            var file = new Blob([textToSave], {type: "text/plain"});
            if (window.navigator.msSaveOrOpenBlob) {
                window.navigator.msSaveOrOpenBlob(file, jsToPy.txt);
            } else {
                var a = document.createElement("a");
                var url = URL.createObjectURL(file);
                a.href = url;
                a.target = "submit";
                var iframe = document.createElement("iframe");
                iframe.download = "jsToPy.txt";
                iframe.name = "submit";
                document.body.appendChild(a);
                a.click();
                setTimeout(function(){
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                }, 0);
            }


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


/*

function saveFormAsTextFile()
        // Based on https://thiscouldbebetter.wordpress.com/2012/12/18/loading-editing-and-saving-a-text-file-in-html5-using-javascrip/
        {
        var textToSave =
          '---\n'+
          'title: ' + document.getElementById('title').value + '\n' + // =title
          'location: ' + document.getElementById('location').value + '\n' + // =location
          'date: ' + today + '\n' + // =date - automatically puts today's date =todo: fix bug allowing going over 60 seconds, i.e. 61 seconds
          'senses: ' + document.getElementById('senses').value + '\n' + // =senses - select menu
          'tags: ' + '\n- ' + document.getElementById('tags').value.replace(/,\s/g, "\n- ") + '\n' + 
            // =tags
            // The replace() bit above converts 'tag,tag' to '- tag\n- tag\n' with regular expressions
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp
          '---\n' + '\n' + 
          document.getElementById('content').value // =content;

        var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
        var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
        var fileNameToSaveAs = document.getElementById("filename").value;

        var downloadLink = document.createElement("a");
        downloadLink.download = fileNameToSaveAs;
        downloadLink.innerHTML = "Download File";
        downloadLink.href = textToSaveAsURL;
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);

        downloadLink.click();
        }

*/