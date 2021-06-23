<?php

$dbconn = pg_connect("host = localhost dbname=postgres user=postgres password=IBM190hooch")
    or die ('Не удалось соединиться: ' . pg_last_error());

if (!$dbconn) {
    echo "Error!!!\n";
}

?>