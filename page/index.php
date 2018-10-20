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

        <?php
        if(isset($_POST['symptoms'])){
            $symptoms = $_POST('symptoms');
            $file = fopen("./io/jsToPy.txt", "w+") or die("file not open");
            fputs($file, $symptoms) or die("data did not write");

            fclose($file);
        }
        ?>

        <div id="wrapper">
            <div id="front">
                <video id="logo" loop autoplay muted> <source src="img/output.webm"></video>
                <h2 id="questions" style="display:visible">Hello! How are you?</h2>
            </div>
            <div id="questionbox">
                <form action="parse_input.php" method="POST">
                    <input type="text" id="symptoms" name="symptoms"/>
                </form>            
            </div>

        </div>

    </body>
</html>