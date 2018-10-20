<?php
$input = $_POST['symptoms'];
$fh = fopen('./io/jsToPy.txt' "a+");
fwrite($fh, $input);
fclose($fh);

?>