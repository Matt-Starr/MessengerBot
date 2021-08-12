<?php

    $hs= "localhost";
    $us= "root";
    $ps= "";
    $SubjectCode = $_POST["subCode"];
    $GroupLink = $_POST["GroupLink"];



    $list = array (
        array($SubjectCode, $GroupLink, 'False'),
    );

    $fp = fopen('Resources\Grouplist.csv', 'a');

    foreach ($list as $fields) {
        fputcsv($fp, $fields);
    }

    fclose($fp);
    echo("Thanks, As long as the bot has been added to the chat your group is registered.");


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