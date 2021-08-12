<!DOCTYPE html>
<html>
<body>

<h1>Join registered group</h1>

<a href="index.html">
    <button>back</button>
</a>

<h3>Which group would you like to join?</h3>
<p>You can only select one at a time, so if you would like to join multiple
    please go back to this page and submit a seperage request</p>
<form name="frmRequests" method="POST" action="requests.php">
    <select name="groupRequest">
        <option selected="selected">Choose one</option>
        <?php
        // A sample product array
        $grouplistcsv = fopen('Resources\Grouplist.csv','r');
        $col = 0;
        $stack = array();
        // while there are more lines, keep doing this
        while(! feof($grouplistcsv))
        {
            // print out the given column of the line
            array_push($stack, fgetcsv($grouplistcsv)[$col]);
        }
        // close the file connection
        fclose($grouplistcsv);
        array_pop($stack);
        
        // Iterating through the product array
        foreach($stack as $item){
            echo '<option value="' . $item . '">' . $item . '</option>';
        }
        ?>

    </select> 

    <h3>What is your Facebook ID?</h3>
    <p>This is the name at the end of the link on your facebook profile</p>

    <img src="Resources\IDlink.png" alt="Trulli"><br><br>
    <label for="fname">Facebook ID:</label>
    <input type="text" id="fbId" name="fbId"><br><br>
    <input type="submit" value="Submit">
</form>

</body>
</html> 