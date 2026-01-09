1. python program

- used beautifulsoup for scraping
- stored into json file as it's better for data serialization, human-readability, also widely adopted
- passing search input from cli itself for simplicity

2. SQL

a) How many types of Acacia plants can be found in the taxonomy table of the dataset?

```
select count(species) from taxonomy where species like '%Acacia%';
  +----------------+
  | count(species) |
  +----------------+
  |            389 |
  +----------------+
  1 row in set (1.344 sec)
```

b) Which type of wheat has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)

```
select t.species, r.description, r.length from rfamseq r
                join taxonomy t on t.ncbi_id = r.ncbi_id
                where t.species like '%wheat%'
                order by r.length desc
                limit 1;
  +------------------------------+---------------------------------------------------------------------------+-----------+
  | species                      | description                                                               | length    |
  +------------------------------+---------------------------------------------------------------------------+-----------+
  | Triticum durum (durum wheat) | LT934116.1 Triticum turgidum subsp. durum genome assembly, chromosome: 3B | 836514780 |
  +------------------------------+---------------------------------------------------------------------------+-----------+
  1 row in set (5.984 sec)
```

c) We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

```
select f.rfam_acc, f.rfam_id, max(r.length) as max_length
                from family f join full_region fr on f.rfam_acc = fr.rfam_acc
                join rfamseq r on fr.rfamseq_acc = r.rfamseq_acc
                where r.length > 1000000
                group by f.rfam_acc, f.rfam_id
                order by max_length desc
                limit 15
                offset 120;
+----------+--------------+------------+
| rfam_acc | rfam_id      | max_length |
+----------+--------------+------------+
| RF01284  | snoR8a       |  836514780 |
| RF00201  | snoZ278      |  836514780 |
| RF01286  | snoR26       |  836514780 |
| RF01856  | Protozoa_SRP |  836514780 |
| RF01300  | snoU49       |  836514780 |
| RF00359  | snoZ102_R77  |  836514780 |
| RF00361  | snoZ119      |  836514780 |
| RF03685  | MIR9677      |  836514780 |
| RF00504  | Glycine      |  836514780 |
| RF03896  | MIR2275      |  836514780 |
| RF01227  | snoR83       |  836514780 |
| RF00695  | MIR398       |  836514780 |
| RF00337  | snoZ112      |  836514780 |
| RF00133  | SNORD33      |  836514780 |
| RF00135  | snoZ223      |  836514780 |
+----------+--------------+------------+
15 rows in set (3 min 6.895 sec) 
```

3. shell script

- shell script is simple and shows output correctly most of the time, but have some flaws for values that are inside inverted commas having commas
