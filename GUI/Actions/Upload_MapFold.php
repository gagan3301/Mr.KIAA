<?php
    /*ORIGINAL CREATOR: Gagan (KIA)
    AUTHOR: Gagan (KIA)
    Copyright (C) 2023 KIA <rtg.gagan@gmail.com>
    */

    $filename = "../Maps/Temp.txt";
    $reader = fopen("../Maps/TempEncode.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?> 

