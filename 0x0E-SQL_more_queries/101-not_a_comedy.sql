-- list all shows without the Comedy genre
SELECT `title` FROM `tv_shows`
WHERE `title` NOT IN (
	SELECT `title` from `tv_genres`
	INNER JOIN `tv_show_genres` on `tv_show_genres`.`genre_id` = `tv_genres`.`id`
	RIGHT JOIN `tv_shows` on `tv_genres`.`show_id` = `tv_shows`.`id`
)
ORDER BY `title`;
