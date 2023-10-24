<?php
    /*ORIGINAL CREATOR:  (KIA)
    AUTHOR:  (KIA)
    Copyright (C) 2023 KIA <>
    */

    $filename = "../Maps/Temp.txt";
    $reader = fopen("../Maps/Temp.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?>
