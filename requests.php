<?php

    $hs= "localhost";
    $us= "root";
    $ps= "";
    $RequestedGroup = $_POST["groupRequest"];
    $FacebookId = $_POST["fbId"];


    $list = array (
        array($FacebookId, $RequestedGroup),
    );

    $waitlist = fopen('Resources\Waitlist.csv', 'a');
    $waitlog = fopen('Resources\Waitlog.csv', 'a');

    foreach ($list as $fields) {
        fputcsv($waitlist, $fields);
        fputcsv($waitlog, $fields);
    }

    fclose($waitlist);
    fclose($waitlog);
    echo("Thanks, you will be put on a waitlist and should join this group shortly");


    //$SubjectCode = 'sample';
    //$GroupLink = 'sample';
/*  $mysqlconnect = mysqli_connect("$hs","$us","$ps");

    if($mysqlconnect === false){
        die("my sql is not connected");
    }
else{
    mysqli_select_db($mysqlconnect, "db_addbot");
    echo("mysql is connected");

    $sql = "INSERT INTO tbl_groups (Id, fldGroupName, fldGroupLink)
    VALUES ('0', '$SubjectCode', '$GroupLink')";
    <?php */
?>