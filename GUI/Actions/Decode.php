<?php
    /*ORIGINAL CREATOR: Gagan, Nand and Irtika
    AUTHOR: Gagan, Nand and Irtika
    Copyright 2022-2023 KIA <>
    */ 

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }
?>