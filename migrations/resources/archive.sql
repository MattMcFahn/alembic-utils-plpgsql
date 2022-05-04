returns int as $$
declare
DECLARE
    source text := 'main.' || table_name;
    sink text := 'archive.' || table_name;
    stmt text;

BEGIN
        stmt := 'with
        archive_all as
            (delete from ' || source || ' src
             where exists (select null from ' || source || ') returning src.*)
        insert into ' || sink || ' select * from archive_all';

    execute stmt;
END;
$$
LANGUAGE 'plpgsql'
