PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE measure (id integer primary key, timestamp integer not null, datetime text not null, room text not null, pushed integer not null, temp real not null);
COMMIT;
