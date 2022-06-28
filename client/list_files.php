<?php
$files = scandir( "labels" );
$files = array_diff($files, [".", "..", ".DS_Store"]);
$js_array = json_encode($files);
echo $js_array;
?>