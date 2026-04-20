# Contributing

## How to add an entry

1. Fork this repository
2. Add your entry to `data/deployments.csv` following the schema in `docs/data_schema.md`
3. Run `python scripts/validate.py` to check your entry passes validation
4. Submit a pull request with a brief description and your source

## Data standards

- **Source required**: Every entry must have a verifiable `source_url`
- **ID format**: `[COUNTRY]-[SECTOR_ABBR]-[NNN]` e.g. `KE-FISH-002`
- **Booleans**: Use `TRUE` / `FALSE`
- **Unknown population**: Enter `0` and note "unknown" in `notes`

## Priority sectors

We especially need entries from: smallholder agricultural AI, rural energy, water treatment, port/customs logistics.

## Contact

Open a GitHub issue or email maggyobuya84@gmail.com
