# issue-linker

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=siegfried-ehret-sonarsource_issue-linker&metric=alert_status)](https://sonarcloud.io/dashboard?id=siegfried-ehret-sonarsource_issue-linker)

## description

Link all tickets from a SCD description from [SonarSource's Jira instance](https://jira.sonarsource.com/).

The SCD description must follow the format we have [here](https://jira.sonarsource.com/browse/SCD-123).

The SCD «Breaks down» into linked tickets. Extracted tickets identifiers are the ones between `===== Release Notes` and `===== Production Notes`.

## installation

Make sure you have [pipenv](https://docs.pipenv.org/).

```
pipenv --python 3.7
pipenv install
```

## execution

The script takes 3 mandatory arguments:

- `--scd=SCD-XXX` with the SCD identifier.
- `--username=my.username` with your Jira username.
- `--password=my.password` with your Jira password.

And an optional one:

- `--dry-run=true` to execute the program without calling the linking API. 

Run the following commands:

```
pipenv shell
python issue-linker.py --scd=<SCD-XXX> --username=<my.username> --password=<my.password>
```

## info

Dependencies:

- [click 7.0](https://click.palletsprojects.com/en/7.x/)
- [jira 2.0](https://jira.readthedocs.io/en/master/index.html)

APIs:

- [Issue link types](https://jira.sonarsource.com/rest/api/2/issueLinkType), also added [here](./issueLinkType.json).
