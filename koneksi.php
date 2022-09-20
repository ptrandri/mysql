<?php

$host = "localhost";
$user = "blog";
$pass = "blog";
$db   = "blog";

$conn = mysqli_connect($host, $user, $pass, $db);
// script cek koneksi
if (!$conn) {
    die("Koneksi Tidak Berhasil: " . mysqli_connect_error());
}
?>
