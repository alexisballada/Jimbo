<?php
$fh = fopen('./io/PyToJs.txt','r');
while ($line = fgets($fh)) {
  echo($line);
}
fclose($fh);
?>