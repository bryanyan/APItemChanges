<?php
$xmlDoc=new DOMDocument();
$xmlDoc->load("champions.xml");

$x=$xmlDoc->getElementsByTagName('link');

//get the q parameter from URL
$q=$_GET["q"];

//lookup all links from the xml file if length of q>0
if (strlen($q)>0) {
  $hint="";
  $count=0;
  for($i=0; $i<($x->length); $i++) {
    $y=$x->item($i)->getElementsByTagName('title');
    if ($y->item(0)->nodeType==1) {
      //find a link matching the search text
      if (stristr($y->item(0)->childNodes->item(0)->nodeValue,$q)) {
        if ($count==5) {
          break;
        }
        if ($hint=="") {
          $hint="<a onclick=document.getElementById('inputarea').value='" . 
          $y->item(0)->childNodes->item(0)->nodeValue . 
          "'>" . 
          $y->item(0)->childNodes->item(0)->nodeValue . "</a>";
        } else {
          $hint=$hint . "<br /><a onclick=document.getElementById('inputarea').value='" . 
          $y->item(0)->childNodes->item(0)->nodeValue . 
          "' target='_blank'>" . 
          $y->item(0)->childNodes->item(0)->nodeValue . "</a>";
          $count += 1;
        }
      }
    }
  }
}

// Set output to "no suggestion" if no hint was found
// or to the correct values
if ($hint=="") {
  $response="no suggestion";
} else {
  $response=$hint;
}

//output the response
echo $response;
?>