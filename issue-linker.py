import re

import click
from jira import JIRA


@click.command()
@click.option('--scd', help='ID of the SonarCloud Deployment, for example SCD-123.', required=True)
@click.option('--username', help='Your Jira username.', required=True)
@click.option('--password', help='Your Jira password.', required=True)
@click.option('--dry-run', help='Run the program without calling the API to link', default=False)
def run(scd, username, password, dry_run):
    jira = authenticate(username, password)
    process(jira, scd, dry_run)


def authenticate(username, password):
    """Authenticate to Jira server"""
    print("Authenticate")
    return JIRA(basic_auth=(username, password), options={'server': 'https://jira.sonarsource.com/'})


def process(jira, scd_key, dry_run):
    """Read SCD content"""
    issue = jira.issue(scd_key)
    description = issue.fields.description

    add = False

    regex = re.compile(r"\[.*\]\s+([A-Z]+-\d+)\s+.*")
    number_of_issues_linked = 0

    for line in [line.strip() for line in description.split("\n")]:
        if line.startswith("===== Release Notes"):
            add = True
        elif line.startswith("===== Production Notes"):
            break
        elif add and len(line) > 0:
            issue_key = regex.search(line).group(1)
            print(issue_key)
            number_of_issues_linked = number_of_issues_linked + 1
            if not dry_run:
                jira.create_issue_link("Breaks down", scd_key, issue_key)

    print(f'Linked {number_of_issues_linked} tickets')


if __name__ == '__main__':
    run()
