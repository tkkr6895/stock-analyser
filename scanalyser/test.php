<?php
$value =  $_REQUEST['value'];
$mystring = passthru("python3 /Applications/XAMPP/xamppfiles/htdocs/stock/test.py".$value);
echo $mystring;
?>