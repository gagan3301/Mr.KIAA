<?php
    /*ORIGINAL CREATOR: Luca Garofalo (KIA)
    AUTHOR: Luca Garofalo (KIA)
    Copyright 2022-2023 KIA <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }
?>