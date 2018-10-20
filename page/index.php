<!DOCTYPE html>
<html>
    <head>
        <title>Jimbo</title>
        <link rel="shortcut icon" type="image/png" href="./img/jimbofav.png"/>
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script type="text/javascript" src="http://code.jquery.com/color/jquery.color-2.1.2.js"></script>
        <script src="js/input.js"></script>

    </head>
    <body>
        <iframe name="submit" style="visibility: hidden; width = 0; height = 0;"></iframe>
        <div id="wrapper">
            <div id="front">
                <video id="logo" loop autoplay muted> <source src="img/output.webm"></video>
                <h2 id="questions" style="display:visible">Hello! How are you?</h2>
            </div>
            <div id="questionbox">
                <form action="parse.php" name="symptoms_form" method="post" target="submit">
                    <input type="text" id="symptoms" name="symptoms"/>
                </form>
            </div>

        </div>

    </body>
</html>