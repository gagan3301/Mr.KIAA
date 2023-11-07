<?php
    /*ORIGINAL CREATOR: Gagan, Nand and Irtika
    AUTHOR: Gagan, Nand and Irtika
    Copyright (C) 2022-2023 KIA <>
    */

    $filename = "../Graphs/Temp.txt";
    $reader = fopen("../Graphs/Temp.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?>