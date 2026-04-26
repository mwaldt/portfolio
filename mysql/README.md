# MySQL


## Sample Data

```
CREATE TABLE sample_data (
    date DATE,
    value DECIMAL(10, 2)
);
INSERT INTO sample_data (date, value)
VALUES
    ('2024-01-01', 10.5),
    ('2024-01-02', 12.3),
    ('2024-01-03', 11.8),
    ('2024-01-04', 14.2),
    ('2024-01-05', 13.5),
    ('2024-01-06', 12.6),
    ('2024-01-07', 13.8),
    ('2024-01-08', 15.1),
    ('2024-01-09', 16.5),
    ('2024-01-10', 17.2);
```

Compute Moving Average
```
SELECT
    data,
    value,
    (SELECT AVG(value)
    FROM sample_data AS s2
    WHERE s2.date BETWEEN DATE_SUB(s1.date,
        INTERVAL 2 DAY) AND s1.date) AS moving_avg
FROM
    sample_data AS s1;
```
