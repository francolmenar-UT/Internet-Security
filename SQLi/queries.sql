-- Get all the tables from a Database
SELECT
    table_schema, GROUP_CONCAT(DISTINCT table_name SEPARATOR ',')
FROM
    information_schema.tables
WHERE
    table_schema != 'mysql' AND table_schema != 'information_schema';


-- Get all the tables with its columns
-- TABLE NAME  | CONCACT
SELECT
    table_name, GROUP_CONCAT(DISTINCT column_name SEPARATOR ',')
FROM
    information_schema.columns
WHERE
    table_schema != 'mysql' AND table_schema != 'information_schema'
GROUP BY
    table_name;


-- Get all the tables and columns in the form TABLE/COLUMN, ....
-- It query just a column called "table_column"
SELECT
    table_column
FROM (
        SELECT
            table_name, GROUP_CONCAT(DISTINCT CONCAT(table_name,'/') , column_name SEPARATOR ',') AS table_column
        FROM
            information_schema.columns
        WHERE
            table_schema != 'mysql' AND table_schema != 'information_schema'
        GROUP BY
            table_name
) AS table_column;


-- Get all the tables and columns concatenated in just one parameter
SELECT
    GROUP_CONCAT( table_column SEPARATOR '////') AS table_column_together
FROM (
    SELECT
        table_column
    FROM (
            SELECT
                table_name, GROUP_CONCAT(DISTINCT CONCAT(table_name,'/') , column_name SEPARATOR ',') AS table_column
            FROM
                information_schema.columns
            WHERE
                table_schema != 'mysql' AND table_schema != 'information_schema'
            GROUP BY
                table_name
    ) AS table_column
) AS table_column_together;

-- Get the password of a given username
SELECT
        password
FROM
        users
WHERE
        username='admin';