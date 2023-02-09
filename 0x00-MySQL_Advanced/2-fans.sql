-- Ranks country origins of bands, ordered by the number of (non-unique) fans.
SELECT origin, SUM(fans) AS num_of_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY num_of_fans DESC;
