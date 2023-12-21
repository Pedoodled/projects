BEGIN;

INSERT INTO randpark_course (name, description, rating_yellow, rating_white, rating_gold, rating_red, rating_blue, record_mens, record_ladies)
VALUES ('Bushwillow', 'Trees', 73.2, 72.4, 71.4, 68.5, 0.0, 64, 73),
	   ('Firethorn', 'Tour course', 74.0, 73.2, 72.4, 70.0, 68.9, 65, 73);
	  
INSERT INTO randpark_teetimes (time)
VALUES ('06:00'),
	   ('06:10');


COMMIT;
