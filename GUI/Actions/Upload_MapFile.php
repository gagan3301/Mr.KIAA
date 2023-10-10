<?php
    /*ORIGINAL CREATOR: Luca Garofalo (KIA)
    AUTHOR: Luca Garofalo (KIA)
    Copyright (C) 2023 KIA <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    $filename = "../Maps/Temp.txt";
    $reader = fopen("../Maps/Temp.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?>
