/*
Enter your query here.
*/
set @x = 21;
SELECT REPEAT("* ", @x := @x - 1) FROM information_schema.tables LIMIT 20;
