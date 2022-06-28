<?php
$target_dir = "labels/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
$uploadOk = 1;

if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}

// Allow certain file formats
if($fileType != "txt") {
  echo "Sorry, only TXT files are allowed.";
  $uploadOk = 0;
}

if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
  } else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
      echo "The file '". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). "' has been uploaded. Please return to the previous page.";
    } else {
      echo "Sorry, there was an error uploading your file.";
    }
  }
?>