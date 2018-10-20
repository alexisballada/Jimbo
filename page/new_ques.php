<?php

$fh = fopen('./io/pyTooJs.txt','r') or die("Unable to open file!");
$line = fgets($fh);
echo fread($fh,filesize("./io/pyToJs.txt"));
fclose($fh);
?>
