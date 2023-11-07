/*ORIGINAL CREATOR: Gagan, Nand and Irtika
AUTHOR: Gagan, Nand and Irtika
Copyright (C) 2023 KIA <>
*/


function download(){
    var text = document.getElementById("Download");
    text.innerHTML="DOWNLOAD WILL START IN 0 SECONDS";
    var clickerLink = document.getElementById("clicker");
    clickerLink.click();
}
function Count(){
    var text = document.getElementById("Download");
    text.innerHTML="DOWNLOAD WILL START IN 5 SECONDS";
    const myTimeout = setTimeout(download, 5000);
}