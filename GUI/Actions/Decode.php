<?php
    /*ORIGINAL CREATOR: Gagan (KIA)
    AUTHOR: Gagan (KIA)
    Copyright 2022-2023 KIA <rtg.gagan@gmail.com>
    */ 

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }
?>