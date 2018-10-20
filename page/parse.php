<?php

if(isset($_POST['symptoms'])) {
    $data = $_POST['symptoms'];
    $ret = file_put_contents('./io/jsToPy.txt', $data, FILE_APPEND | LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}

?>